"""
Usage: get_fasta.py [-o outdir]

-o, --outdir outfile   Output directory [default: ./].

"""
import os
import os.path
from datetime import datetime
from typing import List, Generator

import pandas as pd
import requests
from docopt import docopt
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def main(args):
    outdir = args.get('--outdir')
    os.mkdir(outdir)
    url = "https://www.ebi.ac.uk/ena/browser/api/fasta/textsearch"
    print("Fetching FASTA files")
    responses = fetch_fasta_by_date(url)
    for i, r in enumerate(responses, start=1):
        write_file(r, os.path.join(outdir, f"seqs_{i}.fa.gz"))


def write_file(response: requests.Response, filename: str):
    with open(filename, "wb") as file:
        file.write(response.content)
    print(f"Downloaded sequences to {filename}")


def fetch_fasta_by_date(url: str) -> Generator[requests.Response]:
    params = monthly_query_params(start=datetime(2019,12,1), end=datetime.now())
    session = requests.session()
    adapter = HTTPAdapter(max_retries=Retry(connect=3, backoff_factor=0.5))
    session.mount('https://', adapter)
    with session as s:
        return (s.get(url, params=p) for p in params)


def monthly_query_params(start: datetime, end: datetime) -> List[dict]:
    months = pd.date_range(start, end, freq='MS')
    intervals = [i.strftime("%Y-%m") for i in months]
    return [{
        "domain": "embl-covid19",
        "query": f"collection_date:{i}",
        "gzip": "true",
    } for i in intervals]


if __name__ == "__main__":
    main(docopt(__doc__))

