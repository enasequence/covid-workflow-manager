import requests
from itertools import chain
import subprocess
from pymongo import MongoClient

CLIENT = MongoClient("mongodb://samples-logs-db-svc")
DB = CLIENT.samples


def main():
    records = collect_table_data()
    reordered_records = reorder_top_records(
        records,
        [
            {"acc": "MN908947", "id": "MN908947", "source": "embl-covid19"},
            {"acc": "LR991698", "id": "LR991698", "source": "embl-covid19"},
        ],
    )
    create_tmp_collections(reordered_records)
    update_tmp_phylo_collection()
    update_tmp_lineage_collection()
    copy_to_prod_collections()


def create_tmp_collections(records):
    DB.phylo_tmp.insert_many(records)
    DB.lineage_tmp.insert_many(records)


def collect_table_data():
    """
    This function will collect all records from
    https://www.covid19dataportal.org/sequences?db=embl-covid19 table
    To mirror the table, records MN908947 and LR991698 are shown first.
    :return: list of records to be added to DB in format eg.
    [{'acc': 'MN908947', 'id': 'MN908947', 'source': 'embl-covid19'}, ...]
    """

    url = "https://www.ebi.ac.uk/ebisearch/ws/rest/embl-covid19"
    batch_size = 1000
    base_parameters = {
        "query": "id:[* TO *]",
        "size": str(batch_size),
        "format": "JSON",
        "facetcount": "11",
    }
    total_records = requests.get(url, params=base_parameters).json().get("hitCount")
    batch_parameters = [
        {**base_parameters, "start": i}
        for i in range(batch_size, total_records, batch_size)
    ]
    parameter_list = [
        base_parameters,  # the first request uniquely lacks start argument
        *batch_parameters,
    ]
    return chain.from_iterable(
        [requests.get(url, params=p).json().get("entries") for p in parameter_list]
    )


def reorder_top_records(records, top_records):
    """
    Ensures that specific records are moved to the front of the list of records.
    Also removes duplicates in the final list of dicts.
    :param records: list of dicts
    :param top_records: dicts to move to the front of records
    """
    return deduplicate_dicts([*top_records, *records])


def deduplicate_dicts(l):
    """
    Removes duplicate dicts from a list of dicts, preserving order
    """
    seen = set()
    new_l = []
    for d in l:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            new_l.append(d)
    return new_l


def update_tmp_phylo_collection():
    """
    This function will add information about phylogenetic tree to collection
    and copy new collections to prod
    """
    subprocess.run(
        "wget --backups=1 http://45.86.170.46/coronavirus_sequence.tsv",
        shell=True,
        capture_output=True,
    )
    with open("coronavirus_sequence.tsv", "r") as f:
        next(f)
        for line in f:
            line = line.rstrip()
            data = line.split()
            matrix = data[6]
            accession = data[0]
            if matrix != "None":
                sample = DB.phylo_tmp.find_one({"id": accession})
                if sample is not None:
                    DB.phylo_tmp.update_one(
                        {"id": accession}, {"$set": {"phylogeny": True}}
                    )
                else:
                    DB.suspended_tmp.insert_one({"id": accession})


def update_tmp_lineage_collection():
    """
    Creates a lineage field in the temporary collection, and assigns it the value
    of True or False based on the corresponding record in the pangolin collection.
    Modifies the lineage_tmp collection as a side-effect
    """
    for record in DB.pangolin.find():
        DB.lineage_tmp.update(
            {"id": record["accession"]},
            {"$set": {
                "has_lineage": record["has_lineage"], 
                "lineage": record["lineage"]
            }}
        )


def copy_to_prod_collections():
    """
    Copies the temporary annotated data to final production collections. Finally,
    cleans up temporary collections.
    """
    DB.phylo_tmp.aggregate(pipeline=[{"$match": {}}, {"$out": "phylo"}])
    DB.suspended_tmp.aggregate(pipeline=[{"$match": {}}, {"$out": "suspended"}])
    DB.lineage_tmp.aggregate(pipeline=[{"$match": {}}, {"$out": "lineages_prod"}])

    DB.phylo_tmp.drop()
    DB.suspended_tmp.drop()
    DB.lineage_tmp.drop()


if __name__ == "__main__":
    main()
