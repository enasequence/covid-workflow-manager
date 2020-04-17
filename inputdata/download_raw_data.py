import sys
import os

from pymongo import MongoClient

FIRST_PATTERN = 'ftp.sra.ebi.ac.uk/vol1/'
SECOND_PATTERN = 'ftp.dcc-private.ebi.ac.uk/vol1/'


def main():
    """
    Main function that will parse existing file, check for files existence and
    download all required files
    """
    files_to_download = parse_file()
    for file_name, file_urls in files_to_download.items():
        os.system(f"mkdir /raw_data/{file_name}")
        for file_url in file_urls:
            output_file = f"/raw_data/{file_name}/{os.path.basename(file_url)}"
            os.system(f"wget -t 2 {file_url} -O {output_file}")


def parse_file():
    """
    This function will read output file and generate list of links to download
    :return: list of links to download
    """
    files = dict()
    with open("covid.tsv", 'r') as f:
        next(f)
        for line in f:
            line = line.rstrip()
            data = line.split("\t")
            if not check_file_in_database(data[7]):
                files[data[7]] = generate_download_links(data[10])
    return files


def check_file_in_database(file_name):
    """
    This function will check for current file in MongoDB and insert it in case
    of absence
    :param file_name: name of the file to check
    :return: True if file is already in database and False otherwise
    """
    results = DB.samples.find_one({'id': file_name})
    if results is None:
        DB.samples.insert_one({'id': file_name, 'status': 'new_data'})
        return False
    else:
        return True


def generate_download_links(download_string):
    """
    This function will format download string
    :param download_string: string to reformat
    :return: list of links to download
    """
    files_to_download = list()
    files = download_string.split(';')
    for file_name in files:
        if FIRST_PATTERN in file_name:
            name = file_name.split(FIRST_PATTERN)[-1]
        elif SECOND_PATTERN in file_name:
            name = file_name.split(SECOND_PATTERN)[-1]
        files_to_download.append(f"ftp://{DATA_HUB}:{DATA_HUB_PASSWORD}"
                                 f"@ftp.dcc-private.ebi.ac.uk/vol1/{name}")
    return files_to_download


if __name__ == "__main__":
    # Getting credentials from command line
    DATA_HUB = sys.argv[1]
    DATA_HUB_PASSWORD = sys.argv[2]

    # Getting access to MongoDB
    CLIENT = MongoClient('mongodb://sample-status-db-svc')
    DB = CLIENT.samples
    main()
