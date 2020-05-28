import sys
import datetime
import subprocess
import yaml
import json

from pymongo import MongoClient


def main():
    sample = DB.samples.find_one({'id': RUN})
    write_sample_status(sample, STATUS)
    if STATUS == 'pipeline finished':
        write_sample_status(sample, 'starting to submit export to ENA job')

        # Starting export job
        with open('/wms/submission/jovian-outputdata-job.yaml', 'r') as f:
            job_to_submit = yaml.load(f.read(), Loader=yaml.FullLoader)
            job_to_submit['metadata']['name'] = f"jovian-outputdata-job-" \
                                                f"{RUN.lower()}"
            job_to_submit['spec']['template']['spec']['containers'][0][
                'args'] = [RUN]
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
            write_sample_status(sample, 'submitting export to ENA job failed')
        else:
            write_sample_status(sample, 'submit export to ENA job succeed')
    DB.samples.update_one({'id': RUN}, {'$set': sample})


def write_sample_status(sample, status):
    """
    This function will write date and log message to sample dict
    :param sample: sample to write log to
    :param status: status message
    :return:
    """
    sample['pipeline_analysis']['date'].append(
        datetime.datetime.now().strftime("%d %B, %Y - %H:%M:%S"))
    sample['pipeline_analysis']['status'].append(status)


if __name__ == "__main__":
    # Get run name from command line
    RUN = sys.argv[1]

    # Get status from command line
    STATUS = sys.argv[2]

    # Getting access to MongoDB
    CLIENT = MongoClient('mongodb://samples-logs-db-svc')
    DB = CLIENT.samples
    main()
