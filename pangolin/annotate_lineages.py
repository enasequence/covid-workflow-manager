#!/usr/bin/python
import os, subprocess, datetime, requests, glob, pandas as pd
from urllib.request import urlretrieve
from urllib.parse import urlencode
from pymongo import MongoClient

DB_URI = "mongodb://samples-logs-db-svc"
SEQ_ENDPOINT = "https://www.ebi.ac.uk/ebisearch/ws/rest/embl-covid19"
debug = os.environ.get("DEBUG")


def main():
    if debug == "True":
        minimal_annotate()
    else:
        annotate_new_accessions(remove_old=True)


def minimal_annotate():
    dest_dir = "/data/debug"
    prep_workdir(dest_dir, remove_old=True)
    download_multifasta(["MN908947", "LR991698"], f"{dest_dir}/sequences/seqs_1.fa.gz")
    analyse_multiple(dest_dir)
    result = glob.glob(f"{dest_dir}/output/*.csv")[0]
    df = pd.read_csv(result)
    print(df)


def annotate_new_accessions(remove_old: bool):
    print("Annotating only new records found via REST API")
    dest_dir = "/data/new"
    prep_workdir(dest_dir, remove_old=remove_old)

    accessions = fetch_new_accessions(SEQ_ENDPOINT)
    download_rest(accessions, f"{dest_dir}/sequences")
    analyse_multiple(dest_dir)
    df_list = [parse_results(file) for file in glob.glob(f"{dest_dir}/output/*.csv")]
    df = pd.concat(df_list)
    print(f"Found {len(df)} new records to add")
    save_to_db(df, replace=False)


def prep_workdir(path:str, remove_old: bool):
    subprocess.run(f"mkdir -p {path}", shell=True)
    subdirs = ['sequences', 'output', 'temp']
    for subdir in subdirs:
        subprocess.run(f"mkdir -p {path}/{subdir}", shell=True)
    if remove_old is True:
        for subdir in subdirs:
            subprocess.run(f"rm -rf {path}/{subdir}/*", shell=True)


def fetch_new_accessions(endpoint: str) -> list:
    rest_accession_count = (requests
        .get(endpoint, params={"query": "id:[* TO *]", "format": "JSON"})
        .json()
        .get("hitCount"))
    annotated_accesions = get_annotated_accessions()
    print(f"REST endpoint shows {rest_accession_count} accessions")
    print(f"Found {len(annotated_accesions)} accessions annotated in the database")
    if int(rest_accession_count) == len(annotated_accesions):
        print("No new accessions to annotate, exiting")
        return [] # Don't fetch the accessions if we know there are no new ones

    # fetch all available sequence accessions
    entries = get_paginated_results(endpoint, limit=rest_accession_count)
    all_accessions = [x.get("acc") for x in entries]
    # Return accessions not already in database
    new_accessions = set(all_accessions).difference(annotated_accesions)
    return list(new_accessions)


def get_annotated_accessions() -> list:
    # get all of the annotated accessions from the db
    client = MongoClient(DB_URI)
    db = client.samples
    records = list(db.pangolin.find({}, {"accession": True}))
    return [x.get("accession") for x in records]


def download_rest(accessions: list, directory: str, chunk_size: int = 400):
    # http errors from EBI search if we have more than 400 IDs per request
    if not accessions:
        print("No new accessions to download, exiting")
        return

    print(f"Batch downloading {len(accessions)} new accessions...")
    chunks = [accessions[x:x + chunk_size] for x in range(0, len(accessions), chunk_size)]
    for i, accessions in enumerate(chunks):
        download_multifasta(accessions, f"{directory}/seqs_{i}.fa.gz")


def download_multifasta(accessions: list, filename: str) -> str:
    start = datetime.datetime.now()
    urlretrieve(
        "https://www.ebi.ac.uk/ena/browser/api/fasta/textsearch?" + urlencode({
            "domain": "embl-covid19",
            "query": "id:" + " OR ".join(accessions),
            "limit": len(accessions),
            "gzip": True,
        }),
        filename)
    end = datetime.datetime.now()
    delta = end - start
    print(f"Downloaded {len(accessions)} accessions in {delta.seconds} sec to {filename}")
    return filename


def get_paginated_results(url: str, limit: int, batch_size: int = 1000) -> list:
    parameter_list = [
        {
            "query": "id:[* TO *]",
            "size": str(batch_size),
            "format": "JSON",
            "start": i
        } for i in range(0, limit, batch_size)
    ]
    flatten = lambda t: [item for sublist in t for item in sublist]
    entry_list = [requests.get(url, params=p).json().get("entries") for p in parameter_list]
    return flatten(entry_list)


def analyse_multiple(directory: str):
    for g in glob.glob(f"{directory}/sequences/seqs_*.gz"):
        gunzip = subprocess.run(f"gunzip -f {g}", shell=True)
        gunzip.check_returncode()

    for seq_file in glob.glob(f"{directory}/sequences/seqs_*.fa"):
        process = subprocess.run(
            f"pangolin "
            f"--tempdir {directory}/temp "
            f"--outdir {directory}/output "
            f"--outfile {os.path.basename(seq_file)}.csv "
            f"--min-length 1000 "
            f"{seq_file}",
            shell=True
        )
        process.check_returncode()


def parse_results(csv_file: str) -> pd.DataFrame:
    print(f"parsing {csv_file}")
    df = pd.read_csv(csv_file)[["taxon", "lineage"]]
    print(f"Found {len(df)} rows")
    return (
        df.assign(accession=df.taxon.map(lambda x: x.split("|")[1] or ""))
        .drop(["taxon"], axis=1)
        .assign(has_lineage=df.lineage.map(lambda x: x != "None"))
    )


def save_to_db(df: pd.DataFrame, replace: bool):
    records = df.to_dict("records")
    db = MongoClient(DB_URI).samples
    if replace:
        db.pangolin.drop()
    db.pangolin.insert_many(records)


def log_error(message: str):
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
        upsert=True
    )


if __name__ == "__main__":
    main()
