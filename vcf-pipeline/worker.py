#!/usr/bin/env python

import subprocess
import os
from pymongo import MongoClient

import rediswq


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
            itemstr = item.decode("utf-8")
            print(f"Working on {itemstr}")
            sample = DB.samples.find_one({'id': itemstr})
            # Download data
            os.system(f"mkdir /data/{itemstr}_input")
            os.system(
                f"wget -P /data/{itemstr}_input ftp://{sample['links'][0]}")
            os.system(
                f"wget -P /data/{itemstr}_input ftp://{sample['links'][1]}")
            # Start nextflow
            create_dir_process = subprocess.run(
                f"mkdir -p /data/{itemstr}_output", shell=True,
                capture_output=True)
            os.chdir(f"/data/{itemstr}_output")
            READS = f"/data/{itemstr}_input/{itemstr}_{1, 2}.fastq.gz"
            READS = READS.replace("(", "{")
            READS = READS.replace(")", "}")
            READS = READS.replace(" ", "")
            nextflow_command = f"../nextflow -C ../nextflow.config run " \
                               f"../workflow.nf --READS {READS} " \
                               f"--RUN_ID {itemstr} --resume"
            nextflow_process = subprocess.run(nextflow_command, shell=True)
            # clean temprorary files
            if os.path.exists(
                    f"/data/{itemstr}_output/results/"
                    f"{itemstr}.annot.n.filtered_freq.vcf"):
                remove_work_process = subprocess.run(
                    f"rm -rf ./work", shell=True)
                os.chdir("/data")
                archive_results_process = subprocess.run(
                    f"tar -zcvf {itemstr}_output.tar.gz {itemstr}_output",
                    shell=True)
                move_results_process = subprocess.run(
                    f"mv {itemstr}_output.tar.gz /output", shell=True)
                remove_results_process = subprocess.run(
                    f"rm -rf {itemstr}_output", shell=True)
                remove_raw_data_process = subprocess.run(
                    f"rm -rf {itemstr}_input", shell=True)
            else:
                os.chdir("/data")
                remove_results_process = subprocess.run(
                    f"rm -rf {itemstr}_output", shell=True)
                remove_raw_data_process = subprocess.run(
                    f"rm -rf {itemstr}_input", shell=True)
            q.complete(item)
        else:
            print("Waiting for work")
    print("Queue empty, exiting")
    return


if __name__ == "__main__":
    main()
