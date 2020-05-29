import datetime
import subprocess
import os
import yaml
import json

from pymongo import MongoClient


def main():
    """
    Main function that will parse existing file, check for files existence and
    download all required files
    """
    files_to_download = parse_file()
    for file_name, file_url in files_to_download.items():
        # Updating status of sample
        sample = DB.samples.find_one({'id': file_name})
        write_sample_status(sample, 'download started')

        # Creating directory for raw data
        data_download_errors = list()
        completed_process_mkdir = subprocess.run(
            f"mkdir /data/{file_name}_input", shell=True, capture_output=True)
        if completed_process_mkdir.returncode != 0:
            data_download_errors.append(
                completed_process_mkdir.stderr.decode('utf-8')
            )

        # Download files from ftp
        output_file = f"/data/{file_name}_input/{os.path.basename(file_url)}"
        completed_process_wget = subprocess.run(
            f"wget -t 2 {file_url} -O {output_file}", shell=True,
            capture_output=True)
        if completed_process_wget.returncode != 0:
            data_download_errors.append(
                completed_process_wget.stderr.decode('utf-8')
            )
        write_sample_errors(sample, data_download_errors)
        if len(data_download_errors) > 0:
            write_sample_status(sample, 'download failed')
        else:
            write_sample_status(sample, 'download finished')
            write_sample_status(sample, 'starting to submit pipeline job')

            # Converting yaml to json as required by k8s api server
            with open('/wms/ont-pipeline/ont-pipeline-run-job.yaml', 'r') as f:
                job_to_submit = yaml.load(f.read(), Loader=yaml.FullLoader)
                # Assigning unit id to job (id of run)
                job_to_submit['metadata']['name'] = f"ont-pipeline-run-job-" \
                                                    f"{file_name.lower()}"
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
            if not check_file_in_database(data[7], data[2], data[5], len(data)):
                files[data[7]] = data[10]
    return files


def check_file_in_database(file_name, sample_id, study_id, length):
    """
    This function will check for current file in MongoDB and insert it in case
    of absence
    :param file_name: name of the file to check
    :param sample_id: BioSample id
    :param study_id: Study accession
    :param length: length of the data
    :return: True if file is already in database and False otherwise
    """
    results = DB.samples.find_one({'id': file_name})
    if results is None and study_id == 'PRJEB38388' and length == 12:
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
            'pipeline_name': 'ONT',
            'import_from_ena': {'date': list(), 'status': list(),
                                'errors': list()},
            'pipeline_analysis': {'date': list(), 'status': list(),
                                  'errors': list()},
            'export_to_ena': {'date': list(), 'status': list(),
                              'errors': list()}}


if __name__ == "__main__":
    # Getting access to MongoDB
    CLIENT = MongoClient('mongodb://samples-logs-db-svc')
    DB = CLIENT.samples
    main()
