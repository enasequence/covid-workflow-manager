import sys
import datetime

from pymongo import MongoClient


def main():
    sample = DB.samples.find_one({'id': RUN})
    sample['pipeline_analysis']['date'] = datetime.datetime.now()
    sample['pipeline_analysis']['status'] = STATUS
    DB.samples.update_one({'id': RUN}, {'$set': sample})


if __name__ == "__main__":
    # Get run name from command line
    RUN = sys.argv[1]

    # Get status from command line
    STATUS = sys.argv[2]

    # Getting access to MongoDB
    CLIENT = MongoClient('mongodb://sample-status-db-svc')
    DB = CLIENT.samples
    main()
