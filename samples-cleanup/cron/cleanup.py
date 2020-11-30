"""
Currently after every pipeline run I need to remove pods, jobs and data manually but we need to have microservice that will do this automatically.

Create k8s cron-job that will be fired-up every hour and will:

Check for all samples from inner logging system that have ena_export status success
Remove raw data for this samples
Remove jobs for this samples
Remove pods for this samples
"""

import argparse
import requests
import logging
# import datetime
import subprocess
import os
# import yaml
# import json
from kubernetes import client, config
# from pymongo import MongoClient

# def arg_parse_init():
# parser = argparse.ArgumentParser()
# parser.add_argument('--dryrun',  action='store_true')
logger = logging.getLogger('covid-cleanup')
parser = argparse.ArgumentParser()
parser.add_argument('--dryrun', action="store_true")
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--ont', action='store_true')
parser.add_argument('--jovian', action='store_true')
ARGS = vars(parser.parse_args())

PIPELINE_SUBDOMAINS = {"ont": "/ont",
                       "jovian": "/jovian"}

CURRENT_PIPELINE = []

if(ARGS["ont"]):
    CURRENT_PIPELINE = PIPELINE_SUBDOMAINS['ont']
if(ARGS["jovian"]):
    CURRENT_PIPELINE = PIPELINE_SUBDOMAINS['jovian']

# def arg_var_switch(args):
# DEBUG = True
# CLIENT = MongoClient('mongodb://samples-logs-db-svc')
# DB = CLIENT.samples


INDEX_PAGE = 'http://193.62.54.246'  # Is this local host on the cluster?
API_PATH = '/api'

# ONT_SUBDOMAIN = '/ont'

RESULTS_API = 'results'
PIPELINE_API_STATUS = 'ena_export'
SUCCESS_STATUS = 'export_finished'

API_URL = '{ip}/api/{subpage}'
SAMPLE_PATH = '/data/{file_name}_input'

# /api/ont
# http://193.62.54.246/api/ont


def delete_job(api_instance, job_name, namespace):
    api_response = api_instance.delete_namespaced_job(
        name=job_name,
        namespace=namespace,
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=5))
    print("Job deleted. status='%s'" % str(api_response.status))

def logging_setup():
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('cleanup.log')
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()

    if(ARGS["verbose"]):
        logging.getLogger().setLevel(logging.INFO)
    else:
        ch.setLevel(logging.ERROR)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)


def remove_jobs(samples):
    try:
        config.load_kube_config()
    except:
        # load_kube_config throws if there is no config, but does not document what it throws, so I can't rely on any particular type here
        config.load_incluster_config()

    c = client.Configuration()  # go and get a copy of the default config
    c.verify_ssl = False  # set verify_ssl to false in that config
    # make that config the default for all new clients
    client.Configuration.set_default(c)
    v1 = client.CoreV1Api()
    api = client.ApiClient()

    for sample in samples:
        try:
            sample_name = sample['id']
            job_name = f"ont-pipeline-run-job-{sample_name.lower()}"
            if(ARGS["dryrun"]):
                logger.info(f' DRY - delete_job(api,{job_name},"default")')
            else:
                delete_job(api,job_name,"default")        
        except Exception:
            logger.exception(f'Failed to remove job {job_name}')

def remove_pods(samples):
    # for sample in samples
    pass


def remove_data(samples):
    # results = DB.samples.find_one({'id': file_name})
    for sample in samples:
        try:
            file_name = sample['id']
            folder_path = f"/data/{file_name}_input"
            command = f"rm -R {folder_path}/"
            if(ARGS["dryrun"]):
                logger.info(f" DRY - {str(command)}")
            else:
                if(not(os.path.isdir(folder_path))):
                    logger.exception(f'{folder_path} does not exist')
                    logger.info(str(command))
                else:
                    remove_exported_fin = subprocess.run(command,
                                                         shell=True,
                                                         capture_output=True)
                    if remove_exported_fin.returncode != 0:
                        logger.exception(f'Bad return code')
                        raise Exception
        except Exception:
            logger.exception(f'Failed to remove {file_name}')


def make_api_url(api_url, ip, pipeline_subdomain):
    format_dict = {'ip': ip,
                   'subpage': pipeline_subdomain
                   }
    url = api_url.format(**format_dict)
    return url


# def make_api_subdomain(api_path, pipeline_subdomains, pipline_subdomain):
#     return api_path + pipeline_subdomains.get(pipline_subdomain)


def get_list_of_samples(url):
    session = get_session(url)
    # request = requests.Request('GET', INDEX_PAGE)
    return session.get(url).json()['results']


def filter_samples_by_success(samples):
    return list(filter(
        lambda sample:
            sample["export_to_ena"]['status'] != 'export_finished',
            samples))


def get_session(url):
    with requests.Session() as session:
        request = requests.Request('GET', url)
        prepped = session.prepare_request(request)
        response = session.send(prepped)
        if response.status_code != 200:
            response.raise_for_status()
        return session


def k8s_init():
    config.load_kube_config()
    # config.load_incluster_config()
    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_namespaced_pod("default")
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip,
                              i.metadata.namespace,
                              i.metadata.name))

# def arg_parsing():


def main():
    # Start logging
    logging_setup()
    # arg_parse_init()
    logger.info("Initialise")
    logger.info(ARGS)
    # k8s_init()
    # Make URL
    format_dict = {'ip': INDEX_PAGE, 'subpage': CURRENT_PIPELINE}
    url = API_URL.format(**format_dict)

    logger.info("API url: " + str(url))
    try:
        # Get list of samples
        samples = get_list_of_samples(url)
        logger.info(f"Found {len(samples)} samples")
        # logger.debug("List of samples: " + str(samples))
        # Filter for succesful samples
        logger.info(f"Found {len(samples)} finished samples")
        successful_samples = filter_samples_by_success(samples)
        # logger.debug("List of succesful samples: " + str(successful_samples))
        # Try each of the routines to run on the sample list
        routines = (remove_pods,
                    remove_data,
                    remove_jobs)
        # Cycle through clean-up functions
        for routine in routines:
            try:
                logger.info(f'Starting: {routine.__name__}')
                routine(successful_samples)
                logger.info(f'Finished: {routine.__name__}')
            except Exception:
                logger.exception("Failed on : " + routine.__name__)
    except Exception:
        logger.exception("Failed to get list of samples")


if __name__ == "main":
    main()
# main()
