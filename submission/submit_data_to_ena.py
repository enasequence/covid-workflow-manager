import sys
import subprocess
import time

from lxml import etree

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
    upload_command = f"curl -T {filename}  ftp://webin.ebi.ac.uk " \
                     f"--user {USER}:{PASSWORD}"
    md5_uploaded = f"curl -s ftp://webin.ebi.ac.uk/{filename} " \
                   f"--user {USER}:{PASSWORD} | md5sum | cut -f1 -d ' '"
    md5_original = f"md5sum {filename} | cut -f1 -d ' '"

    # TODO: check last recommendations
    uploadmd5, uploaderr = subprocess.Popen(
        md5_original, shell=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE).communicate()
    out, err = subprocess.Popen(
        upload_command, shell=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE).communicate()
    downloadmd5, downloaderr = subprocess.Popen(
        md5_uploaded, shell=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE).communicate()
    uploadmd5 = uploadmd5.decode().strip(' \t\n\r')
    downloadmd5 = downloadmd5.decode().strip(' \t\n\r')
    if uploadmd5 == downloadmd5:
        # TODO: write error to MongoDB
        pass
    else:
        # TODO: restrict number of attempts
        time.sleep(10)
        upload_files_to_ena(filename)


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
    # TODO: check last recommendations
    sp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    out, err = sp.communicate()
    # TODO: write logs to MongoDB
    submission_error_messages = list()
    if out:
        root = etree.XML(out)
        root = etree.fromstring(out)
        for messages in root.findall('MESSAGES'):
            for mess in messages.findall('ERROR'):
                submission_error_messages.append('ERROR:' + mess.text)

    print("returncode of subprocess:", sp.returncode)


if __name__ == "__main__":
    # Get paths to results from command line
    GZIP_ANALYSIS_FILE = sys.argv[1]
    TAB_ANALYSIS_FILE = sys.argv[2]

    # Get credentials from command line
    USER = sys.argv[3]
    PASSWORD = sys.argv[4]

    # Define XML files
    ANALYSIS_XML = '/analysis.xml'
    SUBMISSION_XML = '/submission.xml'
    ANALYSIS_SUBMISSION_URL_PROD = "https://www.ebi.ac.uk/ena/submit/" \
                                   "drop-box/submit/?auth=ENA"
    ANALYSIS_SUBMISSION_URL_DEV = "https://www-test.ebi.ac.uk/ena/submit/" \
                                  "drop-box/submit/?auth=ENA"
    main()
