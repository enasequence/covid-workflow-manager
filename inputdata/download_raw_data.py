import sys
import os

FIRST_PATTERN = 'ftp.sra.ebi.ac.uk/vol1/'
SECOND_PATTERN = 'ftp.dcc-private.ebi.ac.uk/vol1/'


def main():
    """
    Main function that will parse existing file, check for files existence and
    download all required files
    """
    files_to_download = parse_file()
    for file_name in files_to_download:
        print(file_name)
        os.system(f"wget {file_name}")


def parse_file():
    """
    This function will read output file and generate list of links to download
    :return: list of links to download
    """
    files = list()
    with open("covid.tsv", 'r') as f:
        next(f)
        for line in f:
            line = line.rstrip()
            data = line.split("\t")
            if not check_file_in_database(data[7]):
                files.extend(generate_download_links(data[10]))
    return files


def check_file_in_database(file_name):
    # TODO add connection to db and check
    return False


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
    DATA_HUB = sys.argv[1]
    DATA_HUB_PASSWORD = sys.argv[2]
    main()
