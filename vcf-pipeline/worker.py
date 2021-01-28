#!/usr/bin/env python

import subprocess
import os
import sys

import rediswq
from pymongo import MongoClient


CLIENT = MongoClient('mongodb://samples-logs-db-svc')
DB = CLIENT.samples
HOST = "redis"
q = rediswq.RedisWQ(name="job2", host=HOST)

def main():
    print(f"Worker with sessionID: {q.sessionID()}")
    print(f"Initial queue state: empty = {str(q.empty())}")
    while not q.empty(): # this is never false, never completes
        item = q.lease(lease_secs=10, block=True, timeout=2)
        if item is not None:
            process_item(item)
        else:
            print("Waiting for work")
    print("Queue empty, exiting")
    sys.exit(0)

def process_item(item):
    run_id = item.decode("utf-8")
    print(f"Working on {run_id}")
    sample = get_sample(run_id, DB)
    try:
        links = sample.get('links')
    except KeyError:
        log_error('No links in sample entry')
        raise

    try:
        subprocess.run(f"mkdir -p /data/{run_id}_input", shell=True)
        for link in links:
            subprocess.run(f"wget -P /data/{run_id}_input ftp://{link}", shell=True, check=True)
    except Exception:
        log_error('Download failed')
        raise
    # Start nextflow
    subprocess.run(f"mkdir -p /data/{run_id}_output", shell=True)
    os.chdir(f"/data/{run_id}_output")
    READS = f"/data/{run_id}_input/{run_id}_{1, 2}.fastq.gz"
    READS = READS.replace("(", "{")
    READS = READS.replace(")", "}")
    READS = READS.replace(" ", "")
    nextflow_command = f"../nextflow -C ../nextflow.config run " \
                        f"../workflow.nf --READS {READS} " \
                        f"--RUN_ID {run_id} --resume"
    subprocess.run(nextflow_command, shell=True)
    # clean temprorary files
    if os.path.exists(
            f"/data/{run_id}_output/results/" \
            f"{run_id}.annot.n.filtered_freq.vcf"):
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
    q.complete(item)

def get_sample(run_id, db):
    print(f"Fetching {run_id} record from the database")
    sample = db.samples.find_one({'id': run_id})
    if sample is None:
        raise TypeError("Sample not found in database, aborting")
    return sample

def log_error(message):
    print(f"Error: {message}")
    pass

if __name__ == "__main__":
    main()
