#!/usr/bin/env python

import subprocess
import os

import rediswq
from pymongo import MongoClient


CLIENT = MongoClient('mongodb://samples-logs-db-svc')
DB = CLIENT.samples
HOST = "redis"
q = rediswq.RedisWQ(name="job2", host=HOST)

def main():
    print(f"Worker with sessionID: {q.sessionID()}")
    print(f"Initial queue state: empty = {str(q.empty())}")
    while not q.empty():
        item = q.lease(lease_secs=10, block=True, timeout=2)
        if item is not None:
            run_id = item.decode("utf-8")
            print(f"Working on {run_id}")
            sample = DB.samples.find_one({'id': run_id})
            # Download data
            os.system(f"mkdir /data/{run_id}_input")
            os.system(f"wget -P /data/{run_id}_input ftp://{sample['links'][0]}")
            os.system(f"wget -P /data/{run_id}_input ftp://{sample['links'][1]}")
            # Start nextflow
            create_dir_process = subprocess.run(
                f"mkdir -p /data/{run_id}_output", shell=True,
                capture_output=True)
            os.chdir(f"/data/{run_id}_output")
            READS = f"/data/{run_id}_input/{run_id}_{1, 2}.fastq.gz"
            READS = READS.replace("(", "{")
            READS = READS.replace(")", "}")
            READS = READS.replace(" ", "")
            nextflow_command = f"../nextflow -C ../nextflow.config run " \
                               f"../workflow.nf --READS {READS} " \
                               f"--RUN_ID {run_id} --resume"
            nextflow_process = subprocess.run(nextflow_command, shell=True)
            # clean temprorary files
            if os.path.exists(
                    f"/data/{run_id}_output/results/"
                    f"{run_id}.annot.n.filtered_freq.vcf"):
                remove_work_process = subprocess.run(
                    f"rm -rf ./work", shell=True)
                os.chdir("/data")
                archive_results_process = subprocess.run(
                    f"tar -zcvf {run_id}_output.tar.gz {run_id}_output",
                    shell=True)
                move_results_process = subprocess.run(
                    f"mv {run_id}_output.tar.gz /output", shell=True)
                remove_results_process = subprocess.run(
                    f"rm -rf {run_id}_output", shell=True)
                remove_raw_data_process = subprocess.run(
                    f"rm -rf {run_id}_input", shell=True)
            else:
                os.chdir("/data")
                remove_results_process = subprocess.run(
                    f"rm -rf {run_id}_output", shell=True)
                remove_raw_data_process = subprocess.run(
                    f"rm -rf {run_id}_input", shell=True)
            q.complete(item)
        else:
            print("Waiting for work")
    print("Queue empty, exiting")
    return

def write_sample_status(sample, status):
    """
    This function will write date and log message to sample dict
    :param sample: sample to write log to
    :param status: status message
    :return:
    """
    sample['pipeline_analysis']['date'].append(
        datetime.datetime.now().strftime("%d %B, %Y - %H:%M:%S"))
    sample['pipeline_analysis']['status'].append(status)



if __name__ == "__main__":
    main()
