import requests
import subprocess
from pymongo import MongoClient

CLIENT = MongoClient('mongodb://samples-logs-db-svc')
DB = CLIENT.samples


def main():
    records = collect_table_data()
    create_tmp_collection(records)
    download_files_process = subprocess.run(
        "wget http://45.86.170.46/coronavirus_sequence.tsv", shell=True,
        capture_output=True)
    update_tmp_collection()


def collect_table_data():
    """
    This function will collect all records from
    https://www.covid19dataportal.org/sequences?db=embl-covid19 table
    :return: list of records to be added to DB
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


def create_tmp_collection(records):
    """
    This function will create new collection
    :param records: list of records from data portal
    """
    for record in records:
        DB.phylo_tmp.insert_one(record)


def update_tmp_collection():
    """
    This function will add information about phylogenetic tree to collection
    and copy new collections to prod
    """
    with open('coronavirus_sequence.tsv', 'r') as f:
        next(f)
        for line in f:
            line = line.rstrip()
            data = line.split()
            if data[6] != 'None':
                sample = DB.phylo_tmp.find_one({'id': data[0]})
                if sample is not None:
                    sample['phylogeny'] = True
                    DB.phylo_tmp.update_one({'id': data[0]}, {'$set': sample})
                else:
                    DB.suspended_tmp.insert_one({'id': data[0]})
    # Copy results from tmp collections to prod collections
    DB.phylo_tmp.aggregate(pipeline=[{'$match': {}}, {'$out': 'phylo'}])
    DB.suspended_tmp.aggregate(pipeline=[{'$match': {}}, {'$out': 'suspended'}])
    # Remove tmp collections
    DB.phylo_tmp.drop()
    DB.suspended_tmp.drop()


if __name__ == "__main__":
    main()
