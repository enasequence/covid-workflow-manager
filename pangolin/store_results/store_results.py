# pylint: disable=no-member
"""Usage: store_results.py FILE [options]

FILE                Pangolin output file, csv formatted

Options:

--uri URI           Database URI [default: mongodb://localhost:27017/]
--db DB             Databse name [default: samples]
--collection COL    Database collection [default: pangolin]
--dry-run           Do not connect to database, just print parsed records

"""
from docopt import docopt
import pymongo
import pandas as pd

def main(args: dict):
    df = pd.read_csv(args['FILE'])
    df = df.assign(
        accession=df.taxon.map(lambda x: x.split("|")[1] or ""),
        lineage=df.lineage.map(lambda x: x or "Undetermined"),
        who=df.scorpio_call.map(lambda x: x.split()[0] or ""),
    )
    new_df = df[[
        "accession",
        "lineage",
        "who",
        "scorpio_call",
        "scorpio_support",
        "pangolin_version",
    ]]
    collection = (
        pymongo.MongoClient(args["--uri"])
        [args["--db"]]
        [args["--collection"]]
    )
    if args["--dry-run"]:
        print(new_df)
    else:
        save_to_db(new_df, collection, replace=True)



def save_to_db(
        df: pd.DataFrame,
        collection: pymongo.collection.Collection,
        replace: bool
    ):
    """
    Bulk insert pandas records to a MongoDB collection.
    """
    records = df.to_dict("records")
    if replace:
        collection.drop()
    collection.insert_many(records)


if __name__ == "__main__":
    args = docopt(__doc__)
    main(args)

