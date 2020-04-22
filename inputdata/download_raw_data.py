import sys
import os
import subprocess
import datetime

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
        # Updating status of sample
        sample = DB.samples.find_one({'id': file_name})
        sample['export_from_ena']['date'].append(datetime.datetime.now())
        sample['export_from_ena']['status'].append('download started')
        DB.samples.update_one({'id': file_name}, {'$set': sample})

        # Starting download for every url
        sample = DB.samples.find_one({'id': file_name})
        data_download_errors = list()
        completed_process_mkdir = subprocess.run(
            f"mkdir /raw_data/{file_name}", shell=True, capture_output=True)
        if completed_process_mkdir.returncode != 0:
            data_download_errors.append(
                completed_process_mkdir.stderr.decode('utf-8'))
        # Download should be finished for all files in file_urls
        download_finished_for_urls = 0
        for file_url in file_urls:
            for _ in range(10):
                output_file = f"/raw_data/{file_name}/" \
                              f"{os.path.basename(file_url)}"
                completed_process_wget = subprocess.run(
                    f"wget -t 2 {file_url} -O {output_file}", shell=True,
                    capture_output=True)
                if completed_process_wget.returncode != 0:
                    data_download_errors.append(
                        completed_process_wget.stderr.decode('utf-8'))
                else:
                    download_finished_for_urls += 1
                    break
        sample['export_from_ena']['date'].append(datetime.datetime.now())
        sample['export_from_ena']['errors'].extend(data_download_errors)
        if len(data_download_errors) > 0 and \
                download_finished_for_urls != len(file_urls):
            download_status = 'failed'
        else:
            download_status = 'download finished'
        sample['export_from_ena']['status'].append(download_status)
        DB.samples.update_one({'id': file_name}, {'$set': sample})


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
        sample = get_sample_structure()
        sample['id'] = file_name
        sample['export_from_ena']['date'].append(datetime.datetime.now())
        sample['export_from_ena']['status'].append('run added for download')

        DB.samples.insert_one(sample)
        return False
    else:
        return True


def get_sample_structure():
    """
    This function will return data structure to write to db
    :return:
    """
    return {'id': None,
            'export_from_ena': {'date': list(), 'status': list(),
                                'errors': list()},
            'pipeline_analysis': {'date': list(), 'status': list(),
                                  'errors': list()},
            'import_to_ena': {'date': list(), 'status': list(),
                              'errors': list()}}


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
    CLIENT = MongoClient('mongodb://jovian-sample-status-db-svc')
    DB = CLIENT.samples
    main()
