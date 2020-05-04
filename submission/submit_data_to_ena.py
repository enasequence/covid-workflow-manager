import sys
import subprocess
import time
import datetime
import os

from lxml import etree
from pymongo import MongoClient

from analysis_xml import AnalysisXML
from submission_xml import SubmissionXML
from analysis_file import AnalysisFile


def main():
    """
    Main function to send data to ENA, create XML files and submit them
    """
    sample = DB.samples.find_one({'id': RUN})
    write_sample_status(sample, 'submission to ENA started')
    timestamp = datetime.datetime.now().strftime("%s")
    sample_id = sample['sample_id']
    prefix = f"{RUN}-{timestamp}_{sample_id}_analysis_Rivm_Jovian"

    # Renaming files and results directory
    renaming_errors = list()
    new_filenames = list()
    for filename_src in FILENAMES:
        filename_list = filename_src.split('/')
        filename_list[-1] = f"{prefix}_{filename_src.split('/')[-1]}"
        filename_dest = '/'.join(filename_list)
        new_filenames.append(filename_dest)
        rename_process = subprocess.run(
            f"mv {filename_src} {filename_dest}", shell=True,
            capture_output=True)
        if rename_process.returncode != 0:
            renaming_errors.append(rename_process.stderr.decode('utf-8'))
    if len(renaming_errors) > 0:
        write_sample_errors(sample, renaming_errors)
        DB.samples.update_one({'id': RUN}, {'$set': sample})
        return

    # gzip results directory
    gzip_process = subprocess.run(
        f"tar cvzf {new_filenames[-1]}.tar.gz {new_filenames[-1]}",
        shell=True, capture_output=True)
    if gzip_process.returncode != 0:
        write_sample_errors(sample, [gzip_process.stderr.decode('utf-8')])
        DB.samples.update_one({'id': RUN}, {'$set': sample})
        return

    # Rendering notebook
    write_sample_status(sample, 'started to render notebook')
    # Changing results directory paths
    edit_notebook_process = subprocess.run(
        f"sed -i 's@results@{prefix}_results@g' Notebook_report_k8s.ipynb",
        shell=True, capture_output=True)
    # Executing notebooks
    execute_notebook_process = subprocess.run(
        "jupyter nbconvert --to notebook --execute Notebook_report_k8s.ipynb",
        shell=True, capture_output=True)
    # Converting to html format
    convert_notebook_process = subprocess.run(
        "jupyter nbconvert --to HTML Notebook_report_k8s.nbconvert.ipynb",
        shell=True, capture_output=True)
    if edit_notebook_process.returncode != 0:
        write_sample_status(sample, 'failed to render notebook')
        write_sample_errors(sample, [edit_notebook_process.stderr.decode(
            'utf-8')])
    elif execute_notebook_process.returncode != 0:
        write_sample_status(sample, 'failed to render notebook')
        write_sample_errors(sample, [execute_notebook_process.stderr.decode(
            'utf-8')])
    elif convert_notebook_process != 0:
        write_sample_status(sample, 'failed to render notebook')
        write_sample_errors(sample, [convert_notebook_process.stderr.decode(
            'utf-8')])
    else:
        write_sample_status(sample, 'notebook was rendered successfully')

    # Adding archive type to results folder name
    new_filenames[-1] += '.tar.gz'

    # Creating backup of results directory
    backup_command = f"aws --endpoint-url https://s3.embassy.ebi.ac.uk s3 cp " \
                     f"{new_filenames[-1]} " \
                     f"s3://covid-19-analysis-pipelines-97368143"
    backup_process = subprocess.run(backup_command, shell=True,
                                    capture_output=True)
    if backup_process.returncode != 0:
        write_sample_status(sample, 'Failed to create backup')
        write_sample_errors(sample, [backup_process.stderr.decode('utf-8')])
    else:
        write_sample_status(sample, 'Back created successfully')

    # Uploading files to ENA
    md5_values = dict()
    for new_filename in new_filenames:
        md5_values[new_filename] = upload_files_to_ena(new_filename, sample, 0)
        if sample['export_to_ena']['status'][-1] == f'failed to upload ' \
                                                    f'{new_filename} to ENA':
            write_sample_errors(sample, [f'Failed to upload {new_filename} '
                                         f'to ENA'])
            DB.samples.update_one({'id': RUN}, {'$set': sample})
            return

    # Create xml files
    create_analysis_xml(sample, md5_values, timestamp)
    create_submission_xml(timestamp)

    # Submit xml files to ENA
    submit_xml_files_to_ena(sample)

    DB.samples.update_one({'id': RUN}, {'$set': sample})


def write_sample_status(sample, status):
    """
    This function will write date and log message to sample dict
    :param sample: sample to write log to
    :param status: status message
    :return:
    """
    sample['export_to_ena']['date'].append(
        datetime.datetime.now().strftime("%d %B, %Y - %H:%M:%S"))
    sample['export_to_ena']['status'].append(status)


def write_sample_errors(sample, errors):
    """
    This function will write date and log message to sample dict
    :param sample: sample to write log to
    :param errors: errors list
    :return:
    """
    if len(errors) > 0:
        sample['export_to_ena']['errors'].extend(errors)


def upload_files_to_ena(filename, sample, repeats):
    """
    This function will upload files to ENA
    :param filename: file to upload to ENA
    :param sample: sample from MongoDB to update
    :param repeats: number of repeats
    """
    repeats += 1
    if repeats == 1:
        write_sample_status(sample, f'starting to upload {filename} to ENA')
    upload_command = f"curl -T {filename}  ftp://webin.ebi.ac.uk " \
                     f"--user {USER}:{PASSWORD}"
    md5_uploaded_command = f"curl -s ftp://webin.ebi.ac.uk/{filename} " \
                           f"--user {USER}:{PASSWORD} | md5sum | cut -f1 -d ' '"
    md5_original_command = f"md5sum {filename} | cut -f1 -d ' '"

    completed_process_original = subprocess.run(md5_original_command,
                                                shell=True,
                                                capture_output=True,
                                                timeout=300)
    completed_process_command = subprocess.run(upload_command, shell=True,
                                               capture_output=True, timeout=300)
    completed_process_uploaded = subprocess.run(md5_uploaded_command,
                                                shell=True,
                                                capture_output=True,
                                                timeout=300)
    md5_original = completed_process_original.stdout.decode('utf-8').rstrip()
    md5_uploaded = completed_process_uploaded.stdout.decode('utf-8').rstrip()
    if md5_original == md5_uploaded:
        write_sample_status(sample, f'finishing to upload {filename} to ENA')
        return md5_original
    else:
        time.sleep(10)
        if repeats == 3:
            write_sample_status(sample, f'failed to upload {filename} to ENA')
            return None
        else:
            upload_files_to_ena(filename, sample, repeats)


def create_analysis_xml(sample, md5_values, timestamp):
    """
    This function will generate analysis xml file
    :param sample: sample from MongoDB
    :param md5_values: list of md5 values of files
    :param timestamp: timestamp of analysis
    """
    pipeline_name = "rivm_jovian"
    pipeline_version = "v0.9.6.1"
    alias = f"{pipeline_name}_{RUN.lower()}-{timestamp}"
    centre_name = "COMPARE"
    sample_accession = sample['sample_id']
    study_accession = sample['study_id']
    analysis_date = time.strftime("%Y-%m-%dT%H:%M:%S")
    analysis_files = list()
    for file_name, md5 in md5_values.items():
        file_type = "other" if 'results' in file_name else 'tab'
        analysis_files.append(AnalysisFile(os.path.basename(file_name),
                                           file_type, md5))
    # TODO: check title and description
    title = "Test title"
    description = "Test description"
    analysis_xml_obj = AnalysisXML(alias=alias, centre_name=centre_name,
                                   sample_accession=sample_accession,
                                   run_accession=RUN,
                                   study_accession=study_accession,
                                   pipeline_name=pipeline_name,
                                   pipeline_version=pipeline_version,
                                   analysis_date=analysis_date,
                                   analysis_files=analysis_files, title=title,
                                   description=description,
                                   analysis_xml_file=ANALYSIS_XML)
    analysis_xml_obj.build_xml()


def create_submission_xml(timestamp):
    """
    This function will generate submission xml file
    :param timestamp: timestamp of analysis
    """
    alias = f"sub_{RUN.lower()}-{timestamp}"
    centre_name = 'COMPARE'
    schema = 'analysis'
    # TODO: check action, might be 'MODIFY'
    action = 'ADD'
    analysis_xml_name = os.path.basename(ANALYSIS_XML)
    submission_xml_obj = SubmissionXML(alias=alias,
                                       submission_centre=centre_name,
                                       action=action,
                                       submission_xml_file=SUBMISSION_XML,
                                       source_xml=analysis_xml_name,
                                       schema=schema)
    submission_xml_obj.build_xml()


def submit_xml_files_to_ena(sample):
    """
    This function will submit xml files to ENA
    """
    command = f'curl -k  -F "SUBMISSION=@{SUBMISSION_XML}" ' \
              f'-F "ANALYSIS=@{ANALYSIS_XML}" ' \
              f'"{ANALYSIS_SUBMISSION_URL_DEV}%20{USER}%20{PASSWORD}"'
    completed_process_command = subprocess.run(command, shell=True,
                                               capture_output=True)
    returned_xml = completed_process_command.stdout
    submission_error_messages = list()
    if returned_xml:
        root = etree.XML(returned_xml)
        root = etree.fromstring(returned_xml)
        for messages in root.findall('MESSAGES'):
            for mess in messages.findall('ERROR'):
                submission_error_messages.append('ERROR:' + mess.text)
    if len(submission_error_messages) > 0:
        write_sample_errors(sample, submission_error_messages)
        write_sample_status(sample, 'submission to ENA failed')
    else:
        write_sample_status(sample, 'submission to ENA finished')


if __name__ == "__main__":
    # Get run name from command line
    RUN = sys.argv[1]
    USER = sys.argv[2]
    PASSWORD = sys.argv[3]
    filenames_path = f"/output/{RUN}"
    FILENAMES = [f'{filenames_path}/all_filtered_SNPs.tsv',
                 f'{filenames_path}/all_virusHost.tsv',
                 f'{filenames_path}/all_taxClassified.tsv',
                 f'{filenames_path}/all_taxUnclassified.tsv',
                 f'{filenames_path}/results']

    # Define XML files
    ANALYSIS_XML = f'/output/{RUN}/analysis.xml'
    SUBMISSION_XML = f'/output/{RUN}/submission.xml'
    ANALYSIS_SUBMISSION_URL_PROD = "https://www.ebi.ac.uk/ena/submit/" \
                                   "drop-box/submit/?auth=ENA"
    ANALYSIS_SUBMISSION_URL_DEV = "https://www-test.ebi.ac.uk/ena/submit/" \
                                  "drop-box/submit/?auth=ENA"

    # Getting access to MongoDB
    CLIENT = MongoClient('mongodb://samples-logs-db-svc')
    DB = CLIENT.samples
    main()
