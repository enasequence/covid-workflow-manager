#!/usr/bin/python
import subprocess, wget, pandas as pd
from pymongo import MongoClient

DOWNLOAD = True
ANALYSE = True
PARSE = True
SAVE_TO_DB = True
DB_URI = "mongodb://samples-logs-db-svc"


def main():

    seq_file = "/data/sequences_fasta_latest.fa"
    if DOWNLOAD:
        wget.download(
            f"ftp://ftp.ebi.ac.uk/pub/databases/covid19dataportal/"
            f"viral_sequences/sequences/{seq_file}.gz",
            out="/data/",
        )
        subprocess.run(f"gunzip {seq_file}.gz", shell=True)

    if ANALYSE:
        subprocess.run(
            f"pangolin -o /data/output --tempdir /data/temp --min-length 1000 {seq_file}",
            shell=True,
        )

    if PARSE:
        df = pd.read_csv("/output/lineage_report.csv")[["taxon", "lineage"]]
        records = (
            df.assign(accession=df.taxon.map(lambda x: x.split("|")[1] or ""))
            .drop(["taxon"], axis=1)
            .assign(has_lineage=df.lineage.map(lambda x: x != "None"))
            .to_dict("records")
        )
        print(records[0])

        if SAVE_TO_DB:
            client = MongoClient(DB_URI)
            db = client.samples
            db.pangolin2.insert_many(records)


if __name__ == "__main__":
    main()
