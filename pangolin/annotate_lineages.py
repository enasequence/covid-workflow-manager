#!/usr/bin/python
import subprocess, datetime, pandas as pd
from pymongo import MongoClient

DB_URI = "mongodb://samples-logs-db-svc"
SEQ_FILE = "sequences_fasta_latest.fa"


def main():
    download()
    analyse()
    records = parse_results()
    save_to_db(records)


def download():
    subprocess.run("rm -rf /data/*", shell=True)
    download = subprocess.run(
        f"wget "
        f"ftp://ftp.ebi.ac.uk/pub/databases/covid19dataportal/"
        f"viral_sequences/sequences/{SEQ_FILE}.gz"
        f" -O /data/{SEQ_FILE}.gz",
        shell=True,
        capture_output=True,
    )
    if download.returncode != 0:
        log_error(
            f"There was an error downloading viral sequences "
            f"for annotation: {download.stderr.decode('utf-8')}"
        )
    subprocess.run(f"gunzip /data/{SEQ_FILE}.gz", shell=True)


def analyse():
    subprocess.run(
        f"pangolin -o /data/output --tempdir /data/temp --min-length 1000 /data/{SEQ_FILE}",
        shell=True,
    )


def parse_results():
    df = pd.read_csv("/data/output/lineage_report.csv")[["taxon", "lineage"]]
    return (
        df.assign(accession=df.taxon.map(lambda x: x.split("|")[1] or ""))
        .drop(["taxon"], axis=1)
        .assign(has_lineage=df.lineage.map(lambda x: x != "None"))
        .to_dict("records")
    )


def save_to_db(records):
    client = MongoClient(DB_URI)
    db = client.samples
    db.pangolin.drop()
    db.pangolin.insert_many(records)


def log_error(message):
    db = MongoClient(DB_URI).samples
    timestamp = datetime.datetime.now().strftime("%d %B, %Y - %H:%M:%S")
    db.samples.update_one(
        {"id": "pangolin"},
        {
            "$push": {
                "import.date": timestamp,
                "import.errors": message,
            }
        },
        {"upsert": True}
    )


if __name__ == "__main__":
    main()
