import os, subprocess
import requests
from itertools import chain
from pymongo import MongoClient
import pandas as pd

mongo_uri = os.environ.get("MONGO_URI")
db_name = os.environ.get("DB_NAME", "samples")
if mongo_uri is not None:
    DB = MongoClient(mongo_uri)[db_name]
    print(f"Connected to database {db_name} via {mongo_uri}")


def main():
    """
    sync.py takes the contents of sequence-associated records (phylogeny, lineage)
    and reorders them to the same order of the covid19 sequences endpoint. It saves
    these collections (preserving order) to prod collections, which are served by
    the samples-logs-back-end flask instance as endpoints.
    """
    records = pd.read_csv("/metadata/metadata.tsv", sep="\t").to_dict("record")
    print(f"{len(records)} records to insert: \n{records[:5]}")
    create_tmp_collections(records)

    update_tmp_phylo_collection()
    update_tmp_lineage_collection()
    copy_to_prod_collections()


def create_tmp_collections(records: list):
    DB.phylo_tmp.insert_many(records)
    DB.lineages_tmp.insert_many(records)


def update_tmp_phylo_collection():
    """
    This function will add information about phylogenetic tree to collection
    and copy new collections to prod
    """
    print("Preparing phylogeny endpoint data")
    wget_process = subprocess.run(
        "wget --backups=1 http://45.86.170.46/coronavirus_sequence.tsv",
        shell=True,
        capture_output=True,
    )
    if wget_process.returncode != 0:
        print(
            f"There was a problem downloading the sequences: "
            f"{wget_process.stderr.decode('utf-8')}"
        )
    df = pd.read_table("coronavirus_sequence.tsv")[["Seq_ID", "Matrix"]]
    has_phylo = df.query("Matrix != 'None'")["Seq_ID"].to_list()
    suspended = df.query("Matrix == 'None'")["Seq_ID"].to_list()
    print(f"{len(has_phylo)} accessions have phylogeny results")
    print(
        f"{len(suspended)} accessions do not have phylogeny results and were suspended"
    )
    DB.phylo_tmp.update_many({"id": {"$in": has_phylo}}, {"$set": {"phylogeny": True}})
    DB.suspended_tmp.insert_many([{"id": accession} for accession in suspended])


def update_tmp_lineage_collection():
    """
    Creates a lineage field in the temporary collection, and assigns it the value
    of True or False based on the corresponding record in the pangolin collection.
    Modifies the lineage_tmp collection as a side-effect
    """
    print("Updating lineage values for sequence records")
    pango = list(DB.pangolin.find())
    print(f"Found {len(pango)} lineage annotations to add")
    xref = {i.get("accession"): i.get("lineage") for i in pango}
    temp = DB.lineages_tmp.find()
    new_temp = [set_lineage(r, xref) for r in temp]
    DB.lineages_tmp2.insert_many(new_temp)


def set_lineage(record: dict, xref: dict) -> dict:
    accession_to_annotate = record.get("accession")
    lineage = xref.get(accession_to_annotate)
    if lineage is not None:
        record = record | {"lineage": lineage, "has_lineage": True}
    else:
        record = record | {"has_lineage": False}
    return record


def copy_to_prod_collections():
    """
    Copies the temporary annotated data to final production collections. Finally,
    cleans up temporary collections.
    """
    print("Dropping existing production collections")
    DB.phylo.drop()
    DB.suspended.drop()
    DB.lineages.drop()

    print("Copying re-ordered and annotated records to production collections")
    DB.phylo_tmp.aggregate(pipeline=[{"$match": {}}, {"$out": "phylo"}])
    DB.suspended_tmp.aggregate(pipeline=[{"$match": {}}, {"$out": "suspended"}])
    DB.lineages_tmp2.aggregate(pipeline=[{"$match": {}}, {"$out": "lineages"}])

    print("Removing temporary collections")
    DB.phylo_tmp.drop()
    DB.suspended_tmp.drop()
    DB.lineages_tmp.drop()
    DB.lineages_tmp2.drop()


if __name__ == "__main__":
    main()
