#!/usr/bin/env python

import subprocess
import os
from pymongo import MongoClient

import rediswq


CLIENT = MongoClient('mongodb://mongodb-svc')
DB = CLIENT.samples
HOST = "redis"
q = rediswq.RedisWQ(name="job1", host=HOST)

def main():
    print(f"Worker with sessionID: {q.sessionID()}")
    print(f"Initial queue state: empty = {str(q.empty())}")
    while not q.empty():
        item = q.lease(lease_secs=10, block=True, timeout=2)
        if item is not None:
            itemstr = item.decode("utf-8")
            print(f"Working on {itemstr}")
            sample = DB.samples.find_one({'id': itemstr})
            sample['snapshot'] = '2021_07_26'
            # Download data
            os.system(f"mkdir /data/{itemstr}_input")
            if sample['platform'] == 'illumina':
                if 'ftp.sra.ebi.ac.uk/vol1/' in sample['links'][0]:
                    read_1 = sample['links'][0].replace(
                        'ftp.sra.ebi.ac.uk/vol1/',
                        'https://hh.fire.sdo.ebi.ac.uk/fire/public/era/')
                    read_2 = sample['links'][1].replace(
                        'ftp.sra.ebi.ac.uk/vol1/',
                        'https://hh.fire.sdo.ebi.ac.uk/fire/public/era/')
                elif 'ftp.ebi.ac.uk/vol1/' in sample['links'][0]:
                    read_1 = sample['links'][0].replace(
                        'ftp.ebi.ac.uk/vol1/',
                        'https://hh.fire.sdo.ebi.ac.uk/fire/public/era/')
                    read_2 = sample['links'][1].replace(
                        'ftp.ebi.ac.uk/vol1/',
                        'https://hh.fire.sdo.ebi.ac.uk/fire/public/era/')
                else:
                    read_1 = sample['links'][0]
                    read_2 = sample['links'][1]
                os.system(f"wget -P /data/{itemstr}_input {read_1}")
                os.system(f"wget -P /data/{itemstr}_input {read_2}")
                # Start nextflow
                create_dir_process = subprocess.run(
                    f"mkdir -p /data/{itemstr}_output", shell=True,
                    capture_output=True)
                os.chdir(f"/data/{itemstr}_output")
                READS = f"/data/{itemstr}_input/{itemstr}_{1, 2}.fastq.gz"
                READS = READS.replace("(", "{")
                READS = READS.replace(")", "}")
                READS = READS.replace(" ", "")
                nextflow_command = f"/nextflow -C ../nextflow.config run " \
                                   f"../workflow.nf --READS {READS} " \
                                   f"--RUN_ID {itemstr} --resume"
                nextflow_process = subprocess.run(nextflow_command, shell=True)
            elif sample['platform'] == 'ont':
                if 'ftp.sra.ebi.ac.uk/vol1/' in sample['links'][0]:
                    read = sample['links'][0].replace(
                        'ftp.sra.ebi.ac.uk/vol1/',
                        'https://hh.fire.sdo.ebi.ac.uk/fire/public/era/')
                elif 'ftp.ebi.ac.uk/vol1/' in sample['links'][0]:
                    read = sample['links'][0].replace(
                        'ftp.ebi.ac.uk/vol1/',
                        'https://hh.fire.sdo.ebi.ac.uk/fire/public/era/')
                else:
                    read = sample['links'][0]
                os.system(f"wget -P /data/{itemstr}_input {read}")
                # Start nextflow
                create_dir_process = subprocess.run(
                    f"mkdir -p /data/{itemstr}_output", shell=True,
                    capture_output=True)
                os.chdir(f"/data/{itemstr}_output")
                if os.path.exists(f"/data/{itemstr}_input/{itemstr}.fastq.gz"):
                    input = f"/data/{itemstr}_input/{itemstr}.fastq.gz"
                elif os.path.exists(f"/data/{itemstr}_input/{itemstr}_1.fastq.gz"):
                    input = f"/data/{itemstr}_input/{itemstr}_1.fastq.gz"
                nextflow_command = f"/nextflow -C ../nextflow.config " \
                                   f"run ../nanopore_nextflow.nf " \
                                   f"--INPUT {input} --RUN_ID {itemstr} " \
                                   f"--resume"
                nextflow_process = subprocess.run(nextflow_command, shell=True)
            # clean temprorary files
            if os.path.exists(
                    f"/data/{itemstr}_output/results/"
                    f"{itemstr}.annot.vcf") and os.path.exists(
                f"/data/{itemstr}_output/results/{itemstr}.coverage"):
                sample['pipeline'] = 'success'
                remove_work_process = subprocess.run(
                    f"rm -rf ./work", shell=True)
                remove_data_process = subprocess.run(f"rm -rf ./results/*fq",
                                                     shell=True)
                remove_data_process = subprocess.run(
                    f"rm -rf ./results/*pileup", shell=True)
                move_results_process = subprocess.run(
                    f"cp ./results/{itemstr}.annot.vcf /data/2021_07_26_vcf",
                    shell=True)
                move_results_process = subprocess.run(
                    f"cp ./results/{itemstr}.coverage "
                    f"/data/2021_07_26_coverage", shell=True)
                tar_file_process = subprocess.run(
                    f"gzip /data/2021_07_26_vcf/{itemstr}.annot.vcf",
                    shell=True)
                tar_file_process = subprocess.run(
                    f"gzip /data/2021_07_26_coverage/{itemstr}.coverage",
                    shell=True)
                if os.path.exists(
                        f"/data/{itemstr}_output/results/"
                        f"{itemstr}_consensus.fasta.gz") and \
                        os.path.exists(f"/data/{itemstr}_output/results/"
                                       f"{itemstr}_filtered.vcf.gz"):
                    subprocess.run(
                        f"mv /data/{itemstr}_output/results/"
                        f"{itemstr}_consensus.fasta.gz /data/"
                        f"2021_07_26_consensus_sequences", shell=True)
                    subprocess.run(
                        f"mv /data/{itemstr}_output/results/"
                        f"{itemstr}_filtered.vcf.gz "
                        f"/data/2021_07_26_filtered_vcf", shell=True)
                os.chdir("/data")
                archive_results_process = subprocess.run(
                    f"tar -zcvf {itemstr}_output.tar.gz {itemstr}_output",
                    shell=True)
                remove_results_process = subprocess.run(
                    f"rm -rf {itemstr}_output", shell=True)
                remove_raw_data_process = subprocess.run(
                    f"rm -rf {itemstr}_input", shell=True)
            else:
                sample['pipeline'] = 'failure'
                os.chdir("/data")
                remove_results_process = subprocess.run(
                    f"rm -rf {itemstr}_output", shell=True)
                remove_raw_data_process = subprocess.run(
                    f"rm -rf {itemstr}_input", shell=True)
            DB.samples.update_one({'id': itemstr}, {'$set': sample})
            q.complete(item)
        else:
            print("Waiting for work")
    print("Queue empty, exiting")
    return


if __name__ == "__main__":
    main()
