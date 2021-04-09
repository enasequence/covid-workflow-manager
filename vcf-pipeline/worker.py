#!/usr/bin/env python

import os, sys, subprocess, datetime
from pymongo import MongoClient

import rediswq


CLIENT = MongoClient("mongodb://samples-logs-db-svc")
DB = CLIENT.samples
HOST = "redis"
q = rediswq.RedisWQ(name="job2", host=HOST)


def main():
    print(f"Worker with sessionID: {q.sessionID()}")
    print(f"Initial queue state: empty = {str(q.empty())}")
    while True:
        item = q.lease(lease_secs=10, block=True, timeout=2)
        if item is not None:
            process_item(item)
        else:
            continue
    print("Queue empty, exiting")
    sys.exit(0)


def process_item(item):
    run_id = item.decode("utf-8")
    print(f"Working on {run_id}")

    sample = get_sample(run_id, DB)
    download_files(run_id, sample)
    run_pipeline(run_id)
    clean_up(run_id)

    q.complete(item)


def get_sample(run_id, db):
    print(f"Fetching {run_id} record from the database")
    sample = db.samples.find_one({"id": run_id})
    if sample is None:
        raise TypeError("Sample not found in database, aborting")
    return sample


def download_files(run_id, sample):
    log_status(run_id, f"Starting download for {run_id}")
    try:
        links = sample.get("links")
    except KeyError:
        log_error(run_id, "No links in sample entry")
        raise

    try:
        subprocess.run(f"mkdir -p /data/{run_id}_input", shell=True)
        for count, link in enumerate(links, start=1):
            wget_args = (
                f"--directory-prefix /data/{run_id}_input "
                f"--no-verbose "
                # force overwrite in case this is not the first download attempt
                f"--output-document {run_id}_{count}.fastq.gz "
            )
            subprocess.run(f"wget {wget_args} ftp://{link}", shell=True, check=True)
    except Exception:
        log_error(run_id, "Download failed")
        raise


def run_pipeline(run_id):
    subprocess.run(f"mkdir -p /data/{run_id}_output", shell=True, check=True)
    os.chdir(f"/data/{run_id}_output", check=True)
    reads = clean_read_path(f"/data/{run_id}_input/{run_id}_{1, 2}.fastq.gz")
    nextflow_command = (
        f"../nextflow -C ../nextflow.config run "
        f"../workflow.nf --READS {reads} "
        f"--RUN_ID {run_id} --resume"
    )
    try:
        subprocess.run(nextflow_command, shell=True, check=True)
    except Exception:
        log_error(run_id, "Pipeline failed")
        raise


def clean_read_path(path):
    """
    Replaces braces with curly braces, and removes whitespace
    """
    return path.replace("(", "{").replace(")", "}").replace(" ", "")


def clean_up(run_id):
    if os.path.exists(
        f"/data/{run_id}_output/results/" f"{run_id}.annot.n.filtered_freq.vcf"
    ):
        subprocess.run(f"rm -rf ./work", shell=True)
        os.chdir("/data")
        subprocess.run(f"tar -zcvf {run_id}_output.tar.gz {run_id}_output", shell=True)
        subprocess.run(f"mv {run_id}_output.tar.gz /output", shell=True)
        subprocess.run(f"rm -rf {run_id}_output", shell=True)
        subprocess.run("rm -rf {run_id}_input", shell=True)
    else:
        os.chdir("/data")
        subprocess.run("rm -rf {run_id}_output", shell=True)
        subprocess.run("rm -rf {run_id}_input", shell=True)


def log_status(run_id, status):
    timestamp = datetime.datetime.now().strftime("%d %B, %Y - %H:%M:%S")
    DB.samples.update_one(
        {"id": run_id},
        {
            "$push": {
                "pipeline_analysis.date": timestamp,
                "pipeline_analysis.status": status,
            }
        },
    )


def log_error(run_id, message):
    timestamp = datetime.datetime.now().strftime("%d %B, %Y - %H:%M:%S")
    DB.samples.update_one(
        {"id": run_id},
        {"$push": {"pipeline_analysis.errors": f"{timestamp} -- {message}"}},
    )


if __name__ == "__main__":
    main()
