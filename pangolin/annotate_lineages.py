#!/usr/bin/python
import os, subprocess, datetime, requests, glob, pandas as pd
from urllib.request import urlretrieve
from urllib.parse import urlencode
from pymongo import MongoClient

DB_URI = "mongodb://samples-logs-db-svc"
SEQ_ENDPOINT = "https://www.ebi.ac.uk/ebisearch/ws/rest/embl-covid19"
SOURCE = os.environ.get("SOURCE") # Should be 'ftp' or 'rest'
debug = os.environ.get("DEBUG")


def main():
    if SOURCE == "rest":
        annotate_new_accessions(remove_old=False)
    elif SOURCE == "ftp":
        annotate_all_accessions(remove_old=False)
    else:
        print(f"SOURCE environment variable is {SOURCE}. Should be one of 'ftp', 'rest'. Exiting")


def annotate_new_accessions(remove_old: bool):
    print("Annotating only new records found via REST API")
    dest_dir = "/data/new"
    subprocess.run(f"mkdir -p {dest_dir}", shell=True)
    if remove_old:
        subprocess.run(f"rm -rf {dest_dir}/sequences/*", shell=True)
        subprocess.run(f"rm -rf {dest_dir}/output/*", shell=True)

    accessions = fetch_new_accessions(SEQ_ENDPOINT)
    download_rest(accessions, f"{dest_dir}/sequences")
    analyse_multiple(dest_dir)
    df_list = [parse_results(file) for file in glob.glob(f"{dest_dir}/output/*.csv")]
    df = pd.concat(df_list)
    print(f"Found {len(df)} new records to add")
    save_to_db(df, replace=False)


def annotate_all_accessions(remove_old: bool):
    print("Annotating bulk sequence download from FTP")
    dest_dir = "/data/bulk"
    seq_file = "sequences_fasta_latest.fa" # Do not include .gz extension
    subprocess.run(f"mkdir -p {dest_dir}", shell=True)
    if remove_old:
        subprocess.run(f"rm -rf {dest_dir}/sequences/*", shell=True)
        subprocess.run(f"rm -rf {dest_dir}/output/*", shell=True)
        download_ftp(f"{dest_dir}/sequences", seq_file)

    analyse(dest_dir, seq_file)
    df = parse_results(f"{dest_dir}/output/lineage_report.csv")
    print(f"Total new records to add: {len(df)}")
    save_to_db(df, replace=True)


def download_ftp(dest_dir: str, filename: str):
    download = subprocess.run(
        f"wget ftp://ftp.ebi.ac.uk/pub/databases/covid19dataportal/"
        f"viral_sequences/sequences/{filename}.gz"
        f" -O {dest_dir}/{filename}.gz",
        shell=True,
        capture_output=True,
    )
    print(download.args)
    if download.returncode != 0:
        print(download.stderr.decode('utf-8'))
        log_error(
            f"There was an error downloading viral sequences "
            f"for annotation: {download.stderr.decode('utf-8')}"
        )
    unzip = subprocess.run(f"gunzip {dest_dir}/{filename}.gz", shell=True)
    print(unzip.args)


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
    new_accessions = set(all_accessions).difference(annotated_accesions)
    # Return accessions not already in database
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
    for i, chunk in enumerate(chunks):
        download_from_rest(chunk, f"{directory}/seqs_{i}.fa.gz")


def download_from_rest(accessions: list, filename: str) -> str:
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


def get_paginated_results(url: str, limit: int, batch_size: int =1000) -> list:
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


def analyse(directory: str, seq_file: str):
    process = subprocess.run(
        f"pangolin "
        f"--outdir {directory}/output "
        f"--tempdir {directory}/temp "
        f"--min-length 1000 "
        f"{directory}/sequences/{seq_file}",
        shell=True,
    )
    print(process.args)
    with open(f"{directory}/pangolin.log", 'rw') as f:
        f.write(process.stderr.decode('utf-8'))
    report_errors(process)


def analyse_multiple(directory: str):
    for g in glob.glob(f"{directory}/sequences/seqs_*.gz"):
        gunzip = subprocess.run(f"gunzip {g}", shell=True)
        report_errors(gunzip)

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
        report_errors(process)

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

def report_errors(process: subprocess.CompletedProcess):
    if process.returncode != 0:
        print(process.stderr.decode("utf-8"))

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
