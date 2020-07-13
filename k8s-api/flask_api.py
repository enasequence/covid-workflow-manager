from kubernetes import client, config, utils
from os import path

from kubernetes import client, config, utils
from os import path
from flask_restful import Resource, Api
from pymongo import MongoClient
from flask import Response
from flask import jsonify
# from flask_api import status
from flask_restful import reqparse

from flask import make_response
from flask import request

from flask import Flask

JOB_NAME = "pi"
NAMEPACE = "covid"
YML_JOB_NAME = "k8s-api-job-hello-world"

app = Flask(__name__)
flask_api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('job_name', type=str, help='Job name')
parser.add_argument('namespace', type=str, help='Namespace name')
parser.add_argument('job_body', type=str, help='Serialised json/yml')
# parser.add_argument('delete_pod')


class K8s_api(Resource):

    def post(self):
        """# POST with create jobs"""
        create_job(client.BatchV1Api(), *(parser.parse_args()))
        # yml_path = path.join(path.dirname(__file__), f'{YML_JOB_NAME}.yml')
        # utils.create_from_yaml(client.BatchV1Api(), job_body)
        return f"Created job {args['job_name']}", 200
        return args

    def put(self):
        """# PUT will update a job, if empty it will restart the job?"""
        args = parser.parse_args()
        update_job(client.BatchV1Api(), *args)
        return f"Updated job {args['job_name']}", 200
        return args

    def get(self):
        """ GET will get description of job maybe """
        args = parser.parse_args()
        pass
        return args

    def delete(self):
        """# DELETE will delete jobs"""
        args = parser.parse_args()
        try:
            delete_job(client.BatchV1Api(), **args)
            return f"Deleted job {args['job_name']}", 200
        return eturn args, 400


def create_job_object_test():
    """ # Create dummy job for testing Pod template container """
    container = client.V1Container(
        name="pi",
        image="perl",
        command=["perl", "-Mbignum=bpi", "-wle", "print bpi(2000)"])
    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "pi"}),
        spec=client.V1PodSpec(restart_policy="Never", containers=[container]))
    # Create the specification of deployment
    spec = client.V1JobSpec(
        template=template,
        backoff_limit=4)
    # Instantiate the job object
    job = client.V1Job(
        api_version="batch/v1",
        kind="Job",
        metadata=client.V1ObjectMeta(name=JOB_NAME),
        spec=spec)

    return job


def create_job(api_instance, job_body, job_name, namespace):
    """Create job using the api, job_body, job_name and namespace"""
    api_response = api_instance.create_namespaced_job(
        body=job_body,
        namespace=namespace)
    print("Job created. status='%s'" % str(api_response.status))


def update_job(api_instance, job_body, job_name, namespace):
    """Update job using the api, job_body, job_name and namespace"""
    # Update container image
    # job.spec.template.spec.containers[0].image = "perl"
    api_response = api_instance.patch_namespaced_job(
        name=job_name,
        namespace=namespace,
        body=job_body)
    print("Job updated. status='%s'" % str(api_response.status))


def delete_job(api_instance, job_name, namespace, job_body=None):
    """ Delete job using the api, job_name and namespace, job_body
    should be left blank """
    api_response = api_instance.delete_namespaced_job(
        name=job_name,
        namespace=namespace,
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=5))
    print("Job deleted. status='%s'" % str(api_response.status))


def get_namespace_of_this():
    """ Get namespace of current service. """
    current_namespace = None
    try:
        current_namespace = open(
            "/var/run/secrets/kubernetes.io/serviceaccount/namespace").read()
    except e:
        print("Can't open secrets")
    return current_namespace


def main():

    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.

    try:
        config.load_kube_config()
    except e:
        """# load_kube_config throws if there is no config,
        but does not document what it throws,
        so I can't rely on any particular type here"""
        config.load_incluster_config()

    c = client.Configuration()  # go and get a copy of the default config
    c.verify_ssl = False  # set verify_ssl to false in that config
    # make that config the default for all new clients
    # client.Configuration.set_default(c)
    v1 = client.CoreV1Api()
    api = client.ApiClient()

    # # batch_v1 = client.BatchV1Api()

    # ret = v1.list_namespaced_pod(NAMEPACE)

    # print("Listing pods with their IPs in this namespace:")

    # for i in ret.items:
    #     print("%s\t%s\t%s" %
    #           (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    # print("Listing pods with their IPs all namespaces")

    # ret = v1.list_pod_for_all_namespaces()
    # for i in ret.items:
    #     print("%s\t%s\t%s" %
    #           (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    # batch_v1 = client.BatchV1Api()

    # print("Job demo")

    # jobs_list = batch_v1.list_job_for_all_namespaces()
    # # print(jobs_list)

    # # Create a job object with client-python API. The job we
    # # created is same as the `pi-job.yaml` in the /examples folder.

    # job = create_job_object_test()

    # try:
    #     print("Create job")
    #     create_job(batch_v1, job, NAMEPACE)
    # except:
    #     print("Failed to create job")

    # try:
    #     print("Update job")
    #     update_job(batch_v1, job, JOB_NAME, NAMEPACE)
    # except:
    #     print("Failed to update job")

    # try:
    #     print("Delete job")
    #     delete_job(batch_v1, JOB_NAME, NAMEPACE)
    # except:
    #     print("Failed to delete job")

    # try:
    #     print("create_from_yaml")
    #     yml_path = path.join(path.dirname(__file__), f'{YML_JOB_NAME}.yml')
    #     utils.create_from_yaml(api, yml_path, namespace=NAMEPACE)
    # except:
    #     print("Failed to create job from yml")

    # try:
    #     print("delete_job_yaml")
    #     delete_job(batch_v1, YML_JOB_NAME, NAMEPACE)
    # except:
    #     print("Failed to delete job from yml")

    #     print("Listing pods with their IPs all namespaces")

    # args = {'namespace': NAMEPACE,
    #         'job_name': JOB_NAME,
    #         'job_body': job}

    flask_api.add_resource(K8s_api, '/')
    # k8s_api_obj = K8s_api()
    # k8s_api_obj.delete(args)
    app.run(host='0.0.0.0', debug=True, port=80)
    app.run(debug=True)


if __name__ == '__main__':
    main()
