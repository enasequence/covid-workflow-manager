#!/usr/bin/python
import os, subprocess, datetime, requests, pandas as pd
from re import sub
from urllib.request import urlretrieve
from urllib.parse import urlencode
from itertools import chain
from pymongo import MongoClient

DB_URI = "mongodb://localhost"
SEQ_FILE = "sequences_fasta_latest_temp.fa"
SOURCE = os.environ.get("SOURCE", "ftp") # Should be 'ftp' or 'rest'
DEBUG = True


def main():
    if SOURCE == "rest":
        download_rest()
    else:
        download_ftp()
    # analyse()
    # records = parse_results()
    # save_to_db(records)


def download_ftp():
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


def download_rest():
    # get all available sequence accessions
    if DEBUG:
        with open('test.txt', 'r') as f: rest_accessions =f.read().split("', '")[1:-1]
    else:
        entries = get_paginated_results("https://www.ebi.ac.uk/ebisearch/ws/rest/embl-covid19")
        rest_accessions = [x.get("acc") for x in list(entries)]

    # # get all of the annotated accessions from the db
    # client = MongoClient(DB_URI)
    # db = client.samples
    # records = list(db.pangolin.find({}, {"accession": True}))
    # accessions = [x.get("accession") for x in records]

    # # filter the difference and  download the needed fastas to {SEQ_FILE}
    # difference = list( set(rest_accessions).difference(accessions) )
    # print("Requesting ", ",".join(difference[:5]), "...")

    # req = requests.get("https://www.ebi.ac.uk/ena/browser/api/fasta/textsearch",
    #     params={
    #     "domain": "embl-covid19",
    #     "query": " OR ".join(difference[:1000]),
    #     "limit": 10,
    #     "gzip": True,
    # })

    difference = rest_accessions[:500]
    p = {
        "domain": "embl-covid19",
        "query": " OR ".join(difference),
        "limit": 100,
        "gzip": True,
    }
    start = datetime.datetime.now()
    urlretrieve("https://www.ebi.ac.uk/ena/browser/api/fasta/textsearch?" + urlencode(p), "test.fa.gz")
    end = datetime.datetime.now()
    delta = end - start
    breakpoint()
    print(f"File containing 100,000 sequences downloaded in {delta}")

    import time
    time.sleep(999999)


def get_paginated_results(url, batch_size=1000):
    total_records = requests.get(url, params={"query": "id:[* TO *]", "format": "JSON"}).json().get("hitCount")
    parameter_list = [
        {        
            "query": "id:[* TO *]",
            "size": str(batch_size),
            "format": "JSON",
            "start": i
        } for i in range(0, total_records, batch_size)
    ]
    return chain.from_iterable(
        [requests.get(url, params=p).json().get("entries") for p in parameter_list]
    )


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
