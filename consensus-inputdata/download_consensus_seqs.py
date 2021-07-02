#!/usr/bin/python
import subprocess
from urllib.request import urlretrieve
from urllib.parse import urlencode
import pandas as pd


def main():
    subprocess.run("rm /data/*.fasta", shell=True, check=True)
    get_tsv()
    df = pd.read_csv('/data/metadata.tsv', sep="\t", quoting=True)
    total = len(df)
    get_all_fasta_batched(total=total, chunk_size=100_000)


def get_tsv():
    """
    Downloads a tsv summary of the fasta files, one accession per row in the format:
    accession, description
    """
    url = "https://www.ebi.ac.uk/ena/browser/api/tsv/textsearch?"
    params = {
        "domain": "embl-covid19",
        "query": "id:[* TO *]",
    }
    print("Downloading metadata.tsv")
    urlretrieve(url + urlencode(params), filename="/data/metadata.tsv")


def get_all_fasta_batched(total: int, chunk_size: int):
    endpoint = "https://www.ebi.ac.uk/ena/browser/api/fasta/textsearch?"
    offsets = range(0, total, chunk_size)
    print(f"Downloading {total:,} records in chunks of {chunk_size:,}")
    for i, offset in enumerate(offsets):
        params = {
            "domain": "embl-covid19",
            "query": "id:[* TO *]",
            "offset": offset,
            "limit": chunk_size,
        }
        full_url = endpoint + urlencode(params)
        print(f"Fetching {full_url}")
        urlretrieve(full_url, filename=f"/data/{i}.fasta")


if __name__ == "__main__":
    main()
