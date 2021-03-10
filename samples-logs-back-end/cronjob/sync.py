import requests
import subprocess
from pymongo import MongoClient

CLIENT = MongoClient('mongodb://samples-logs-db-svc')
DB = CLIENT.samples


def main():
    records = collect_table_data()
    create_tmp_collections(records)
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
    :return: list of records to be added to DB in format eg.
    [{'acc': 'MN908947', 'id': 'MN908947', 'source': 'embl-covid19'}, ...]
    """
    first_response = requests.get(
        "https://www.ebi.ac.uk/ebisearch/ws/rest/embl-covid19/"
        "?size=1000&format=JSON&facetcount=11&query=id%3A%5B*%20TO%20*%5D"
    ).json()
    results = list()
    for i in range(0, first_response['hitCount'], 1000):
        if i == 0:
            for record in first_response['entries']:
                results.append(record)
        else:
            response = requests.get(
                f"https://www.ebi.ac.uk/ebisearch/ws/rest/embl-covid19/"
                f"?start={i}&size=1000&format=JSON&facetcount=11"
                f"&query=id%3A%5B*%20TO%20*%5D").json()
            for record in response['entries']:
                results.append(record)
    return results


def update_tmp_phylo_collection():
    """
    This function will add information about phylogenetic tree to collection
    and copy new collections to prod
    """
    subprocess.run(
        "wget --backups=1 http://45.86.170.46/coronavirus_sequence.tsv",
        shell=True,
        capture_output=True)
    with open('coronavirus_sequence.tsv', 'r') as f:
        next(f)
        for line in f:
            line = line.rstrip()
            data = line.split()
            matrix = data[6]
            accession = data[0]
            if matrix != 'None':
                sample = DB.phylo_tmp.find_one({'id': accession})
                if sample is not None:
                    DB.phylo_tmp.update_one(
                        {'id': accession},
                        {'$set': {'phylogeny': True} })
                else:
                    DB.suspended_tmp.insert_one({'id': accession})


def update_tmp_lineage_collection():
    """
    Creates a lineage field in the temporary collection, and assigns it the value
    of True or False based on the corresponding record in the pangolin collection.
    Modifies the lineage_tmp collection as a side-effect
    """
    for record in DB.pangolin.find():
        DB.lineage_tmp.update(
            {'id': record['accession']},
            {'$set': {'lineage': record['has_lineage']} })


def copy_to_prod_collections():
    """
    Copies the temporary annotated data to final production collections. Finally,
    cleans up temporary collections.
    """
    DB.phylo_tmp.aggregate(pipeline=[{'$match': {}}, {'$out': 'phylo'}])
    DB.suspended_tmp.aggregate(pipeline=[{'$match': {}}, {'$out': 'suspended'}])
    DB.lineage_tmp.aggregate(pipeline=[{'$match': {}}, {'$out': 'lineages_prod'}])

    DB.phylo_tmp.drop()
    DB.suspended_tmp.drop()
    DB.lineage_tmp.drop()


if __name__ == "__main__":
    main()
