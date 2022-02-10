# pylint: disable=no-member
"""
Usage: prepreocess_metadata.py <metadata.tsv> [-o outfile.tsv]

Options:
-o, --outfile outfile.tsv   The output file, in tsv format. Should have columns:
                            accession, date, country. [default: results.tsv]

"""
from docopt import docopt
import pandas as pd
import pycountry_convert as pc
from typing import Optional


def main(args: dict):
    df = pd.read_csv(args["<metadata.tsv>"], sep="\t")
    parse_entries(df).to_csv(args["--outfile"], sep="\t", index=None)
    print(f"Wrote {len(df)} records to {args['--outfile']}")


def parse_entries(df: pd.DataFrame) -> pd.DataFrame:
    new_df = df.assign(
        name=df.accession_id,
        virus="ncov",
        date=df.collection_date.astype(str).map(format_date, na_action='ignore'),
        center_name=df.center_name,
        country=df.country,
        region=df.country.map(country_to_region, na_action='ignore'),
    )
    keep_columns = ["name", "date", "virus", "center_name",  "country", "region"]
    return new_df[keep_columns]


def format_date(date: Optional[str]) -> Optional[str]:
    if date and len(date) == 8:
        year = date[:4]
        month = date[4:6].replace("00", "XX")
        day = date[6:].replace("00", "XX")
        return f"{year}-{month}-{day}"
    else:
        return None


def country_to_region(country: Optional[str]) -> str:
    try:
        country_code = pc.country_name_to_country_alpha2(country)
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        region = pc.convert_continent_code_to_continent_name(continent_code)
    except (KeyError, TypeError) as e:
        print(f"Error converting {country} to region, setting to '?'")
        print(e)
        return "?"
    return region

if __name__ == "__main__":
    main(docopt(__doc__))
