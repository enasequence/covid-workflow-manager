import sys
import os
import subprocess
import datetime
import yaml
import json

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
        write_sample_status(sample, 'download started')

        # Starting download for every url
        data_download_errors = list()
        completed_process_mkdir = subprocess.run(
            f"mkdir /raw_data/{file_name}", shell=True, capture_output=True)
        if completed_process_mkdir.returncode != 0:
            data_download_errors.append(
                completed_process_mkdir.stderr.decode('utf-8'))

        # Download should be finished for all files in file_urls,
        # ex. 2 for pair-end and 1 for single-end reads
        download_finished_for_urls = 0
        for file_url in file_urls:
            # 10 attempts to do authentication with ftp server
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
        write_sample_errors(sample, data_download_errors)
        if len(data_download_errors) > 0 and \
                download_finished_for_urls != len(file_urls):
            write_sample_status(sample, 'download failed')
        else:
            write_sample_status(sample, 'download finished')
            write_sample_status(sample, 'starting to submit pipeline job')

            # Converting yaml to json as required by k8s api server
            with open('/wms/pipeline/run_pipeline-job/'
                      'jovian-pipeline-run-job.yaml', 'r') as f:
                job_to_submit = yaml.load(f.read(), Loader=yaml.FullLoader)
                # Assigning unique id to job (id of run)
                job_to_submit['metadata']['name'] = f'jovian-pipeline-run-' \
                                                    f'job-{file_name.lower()}'
                # Submitting run id as arg to job
                job_to_submit['spec']['template']['spec']['containers'][0][
                    'args'] = [file_name]
                job_to_submit = json.dumps(job_to_submit)

            # Get token, required by k8s api server to submit jobs
            get_token_process = subprocess.run(
                "cat /var/run/secrets/kubernetes.io/serviceaccount/token",
                shell=True, capture_output=True)
            k8s_token = get_token_process.stdout.decode('utf-8')

            submit_job_process = subprocess.run(
                f'curl -X POST -sSk -H "Authorization: Bearer {k8s_token}" '
                f'-H "Content-Type: application/json" '
                f'https://$KUBERNETES_SERVICE_HOST:'
                f'$KUBERNETES_PORT_443_TCP_PORT/apis/batch/v1/namespaces/'
                f'default/jobs -d \'{job_to_submit}\'',
                shell=True, capture_output=True)
            submit_job_process_results = json.loads(
                submit_job_process.stdout.decode('utf-8'))
            if submit_job_process_results['status'] == 'Failure':
                write_sample_status(sample, 'submitting pipeline job failed')
                write_sample_errors(sample, [
                    submit_job_process_results['message']
                ])
            else:
                write_sample_status(sample, 'submitting pipeline job succeed')
        DB.samples.update_one({'id': file_name}, {'$set': sample})


def write_sample_status(sample, status):
    """
    This function will write date and log message to sample dict
    :param sample: sample to write log to
    :param status: status message
    :return:
    """
    sample['import_from_ena']['date'].append(
        datetime.datetime.now().strftime("%d %B, %Y - %H:%M:%S"))
    sample['import_from_ena']['status'].append(status)


def write_sample_errors(sample, errors):
    """
    This function will write date and log message to sample dict
    :param sample: sample to write log to
    :param errors: errors list
    :return:
    """
    if len(errors) > 0:
        sample['import_from_ena']['errors'].extend(errors)


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
            if not check_file_in_database(data[7], data[2], data[5]):
                files[data[7]] = generate_download_links(data[10])
    return files


def check_file_in_database(file_name, sample_id, study_id):
    """
    This function will check for current file in MongoDB and insert it in case
    of absence
    :param file_name: name of the file to check
    :param sample_id: BioSample id
    :param study_id: Study accession
    :return: True if file is already in database and False otherwise
    """
    results = DB.samples.find_one({'id': file_name})
    if results is None:
        sample = get_sample_structure()
        sample['id'] = file_name
        sample['sample_id'] = sample_id
        sample['study_id'] = study_id
        sample['import_from_ena']['date'].append(
            datetime.datetime.now().strftime("%d %B, %Y - %H:%M:%S"))
        sample['import_from_ena']['status'].append('run added for download')

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
            'sample_id': None,
            'study_id': None,
            'import_from_ena': {'date': list(), 'status': list(),
                                'errors': list()},
            'pipeline_analysis': {'date': list(), 'status': list(),
                                  'errors': list()},
            'export_to_ena': {'date': list(), 'status': list(),
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
    CLIENT = MongoClient('mongodb://samples-logs-db-svc')
    DB = CLIENT.samples
    main()
