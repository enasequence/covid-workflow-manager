"""
Usage: get_seq_metadata.py [-o outfile] [-n N]

-o, --outfile outfile   Output filename [default: ./lineages.tsv].
-n N, --limit N         Limit the number of records fetched.

"""
from docopt import docopt
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from io import StringIO
import pandas as pd
from csv import QUOTE_ALL
from datetime import date, datetime
from typing import List, Optional
from urllib.parse import parse_qs, urlparse

size_limit = 2_000_000

def main(args):
    url = "https://www.covid19dataportal.org/api/backend/ebisearch"
    outfile = args["--outfile"]
    total = get_entry_count(url)
    responses = fetch_seq_data_by_date(url, limit=args["--limit"])
    df = collect_dataframes(responses)
    record_count = len(df)
    if record_count < total:
        p = record_count / total
        print(
            f"Warning: Only retrieved {record_count:,} of {total:,} total records, ({p:.2%})"
        )
    df.to_csv(outfile, sep="\t", index=None)
    print(df)
    print(f"\033[1;32;40m ✓ Wrote {record_count:,} records to {outfile}")


def get_entry_count(url: str) -> str:
    url = "https://www.ebi.ac.uk/ebisearch/ws/rest/embl-covid19"
    p = {"query": "id:[* TO *]", "size": 1, "format": "JSON"}
    total = requests.get(url, params=p).json().get("hitCount")
    print(f"{total:,} total records available")
    return total


def fetch_seq_data_by_date(url: str, limit: str) -> List[requests.Response]:
    params = params_for(
        start=datetime(2019, 12, 1),
        end=datetime.now(),
        fields=f"acc,collection_date,country,center_name,coverage,"
        f"lineage,phylogeny,who",
    )
    session = requests.session()
    session.mount(
        "https://", HTTPAdapter(max_retries=Retry(connect=3, backoff_factor=0.5))
    )
    with session as s:
        responses = (s.get(url, params=p) for p in params)
    if limit:
        print(f"Limiting to first {limit} requests")
        return [next(responses) for _ in range(int(limit))]
    return responses


def to_df(res: requests.Response) -> Optional[pd.DataFrame]:
    if res.ok is not True:
        print(res.status_code, res.reason)
        return None  # continue
    if len(res.text) == 0:
        params = parse_qs(urlparse(res.url).query)
        print(f"Skipping empty response for {params.get('query')}")
        return None
    if res.headers.get("X-EBI-Search-Total-Results") != "0":
        df = pd.read_table(StringIO(res.text), quoting=QUOTE_ALL)
        print(f"Retrieved {len(df)} records")
        if len(df) == size_limit:
            print(f"Warning, more than {size_limit} found for {res.request.url}")
        return df


def collect_dataframes(responses: List[requests.Response]) -> Optional[List[pd.DataFrame]]:
    dfs = [to_df(r) for r in responses]
    if not any(dfs):
        print("Error: All responses were empty")
        return None
    else:
        return pd.concat(dfs)


def params_for(start: datetime, end: datetime, fields: str) -> list[dict]:
    months = pd.date_range(start, end, freq="MS")
    intervals = [i.strftime("%Y-%m") for i in months]
    return [
        {
            "domain": "embl-covid19",
            "query": f"collection_date:{i}",
            "fields": fields,
            "format": "tsv",
            "gzip": "true",
            "size": size_limit,
        }
        for i in intervals
    ]


def format_date(date: str) -> str:
    if pd.isnull(date):
        return "?"
    year = date[:4]
    month = date[4:6].replace("00", "XX")
    day = date[6:].replace("00", "XX")
    return f"{year}-{month}-{day}"


if __name__ == "__main__":
    args = docopt(__doc__)
    main(args)
