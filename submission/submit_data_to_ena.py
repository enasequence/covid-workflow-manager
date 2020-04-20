import sys
import subprocess
import time
import datetime

from lxml import etree
from pymongo import MongoClient

from .analysis_xml import AnalysisXML
from .submission_xml import SubmissionXML


def main():
    """
    Main function to send data to ENA, create XML files and submit them
    """
    upload_files_to_ena(GZIP_ANALYSIS_FILE)
    upload_files_to_ena(TAB_ANALYSIS_FILE)
    create_analysis_xml()
    create_submission_xml()
    submit_xml_files_to_ena()


def upload_files_to_ena(filename):
    """
    This function will upload files to ENA
    :param filename: file to upload to ENA
    """
    global REPEATS
    REPEATS += 1
    upload_command = f"curl -T {filename}  ftp://webin.ebi.ac.uk " \
                     f"--user {USER}:{PASSWORD}"
    md5_uploaded_command = f"curl -s ftp://webin.ebi.ac.uk/{filename} " \
                           f"--user {USER}:{PASSWORD} | md5sum | cut -f1 -d ' '"
    md5_original_command = f"md5sum {filename} | cut -f1 -d ' '"

    completed_process_original = subprocess.run(md5_original_command,
                                                shell=True, capture_output=True)
    completed_process_command = subprocess.run(upload_command, shell=True,
                                               capture_output=True)
    completed_process_uploaded = subprocess.run(md5_uploaded_command,
                                                shell=True, capture_output=True)
    md5_original = completed_process_original.stdout.decode('utf-8').rstrip()
    md5_uploaded = completed_process_uploaded.stdout.decode('utf-8').rstrip()
    sample = DB.samples.find_one({'id': RUN})
    if md5_original == md5_uploaded:
        sample['import_to_ena']['date'] = datetime.datetime.now()
        sample['import_to_ena']['status'] = 'success'
    else:
        time.sleep(10)
        if REPEATS == 3:
            sample['import_to_ena']['date'] = datetime.datetime.now()
            sample['import_to_ena']['status'] = 'failed'
            sample['import_to_ena']['errors'] = [
                completed_process_command.stderr.decode('utf-8')]
        else:
            upload_files_to_ena(filename)
    DB.samples.update_one({'id': RUN}, {'$set': sample})


def create_analysis_xml():
    """
    This function will generate analysis xml file
    """
    analysis_xml_obj = AnalysisXML()
    analysis_xml_obj.build_xml()


def create_submission_xml():
    """
    This function will generate submission xml file
    """
    submission_xml_obj = SubmissionXML()
    submission_xml_obj.build_xml()


def submit_xml_files_to_ena():
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
    sample = DB.samples.find_one({'id': RUN})
    if len(submission_error_messages) > 0:
        sample['import_to_ena']['date'] = datetime.datetime.now()
        sample['import_to_ena']['status'] = 'failed'
        sample['import_to_ena']['errors'] = submission_error_messages
    else:
        sample['import_to_ena']['date'] = datetime.datetime.now()
        sample['import_to_ena']['status'] = 'success'
    DB.samples.update_one({'id': RUN}, {'$set': sample})


if __name__ == "__main__":
    # Get paths to results from command line
    GZIP_ANALYSIS_FILE = sys.argv[1]
    TAB_ANALYSIS_FILE = sys.argv[2]

    # Get run name from command line
    RUN = sys.argv[3]

    # Get credentials from command line
    USER = sys.argv[4]
    PASSWORD = sys.argv[5]

    # Define XML files
    ANALYSIS_XML = '/analysis.xml'
    SUBMISSION_XML = '/submission.xml'
    ANALYSIS_SUBMISSION_URL_PROD = "https://www.ebi.ac.uk/ena/submit/" \
                                   "drop-box/submit/?auth=ENA"
    ANALYSIS_SUBMISSION_URL_DEV = "https://www-test.ebi.ac.uk/ena/submit/" \
                                  "drop-box/submit/?auth=ENA"

    # Number of attempts of data submission to ENA
    REPEATS = 0

    # Getting access to MongoDB
    CLIENT = MongoClient('mongodb://sample-status-db-svc')
    DB = CLIENT.samples
    main()
