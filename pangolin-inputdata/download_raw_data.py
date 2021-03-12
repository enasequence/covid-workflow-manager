#!/usr/bin/python
import subprocess, wget, pandas as pd
from pymongo import MongoClient

DOWNLOAD = False
ANALYSE = False
PARSE = True
SAVE_TO_DB = False
DB_URI = "mongodb://localhost"


def main():
    # https://www.ebi.ac.uk/ena/browser/api/fasta/textsearch?domain=embl-covid19&query=id%3A%5B*%20TO%20*%5D&limit=5

    """
    1. Download list of ids
    2. Check each id, if in db, next, else download
    3. Run pangolin
    4. Open tsv output and save to db
    """

    seq_file = "/data/sequences_fasta_latest.fa"
    if DOWNLOAD:
        wget.download(
            # f"ftp://ftp.ebi.ac.uk/pub/databases/covid19dataportal/"
            # f"viral_sequences/README.md",
            f"ftp://ftp.ebi.ac.uk/pub/databases/covid19dataportal/"
            f"viral_sequences/sequences/{seq_file}.gz",
            out="/data/",
        )
        subprocess.run(f"gunzip {seq_file}.gz", shell=True)

    if ANALYSE:
        subprocess.run(
            f"pangolin -o /output --tempdir /temp --min-length 1000 {seq_file}",
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
            db.pangolin.insert_many(records)


if __name__ == "__main__":
    main()
