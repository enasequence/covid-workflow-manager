from kubernetes import client, config, utils
from os import path

JOB_NAME = "pi"
NAMEPACE = "covid"
YML_JOB_NAME = "k8s-api-job-hello-world"

def create_job_object():
    # Configureate Pod template container
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


def create_job(api_instance, job):
    api_response = api_instance.create_namespaced_job(
        body=job,
        namespace=NAMEPACE)
    print("Job created. status='%s'" % str(api_response.status))


def update_job(api_instance, job):
    # Update container image
    job.spec.template.spec.containers[0].image = "perl"
    api_response = api_instance.patch_namespaced_job(
        name=JOB_NAME,
        namespace=NAMEPACE,
        body=job)
    print("Job updated. status='%s'" % str(api_response.status))


def delete_job(api_instance,job_name,namespace):
    api_response = api_instance.delete_namespaced_job(
        name=job_name,
        namespace=namespace,
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=5))
    print("Job deleted. status='%s'" % str(api_response.status))


def main():

    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.

    try:
        config.load_kube_config()
    except:
        # load_kube_config throws if there is no config, but does not document what it throws, so I can't rely on any particular type here
        config.load_incluster_config()

    c = client.Configuration()  # go and get a copy of the default config
    c.verify_ssl = True  # set verify_ssl to false in that config
    # make that config the default for all new clients
    client.Configuration.set_default(c)
    v1 = client.CoreV1Api()
    api = client.ApiClient()

    try:
        current_namespace = open(
            "/var/run/secrets/kubernetes.io/serviceaccount/namespace").read()
    except:
        current_namespace = NAMEPACE
        print("Can't open secrets")

    # batch_v1 = client.BatchV1Api()

    ret = v1.list_namespaced_pod(current_namespace)

    print("Listing pods with their IPs in this namespace:")

    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    print("Listing pods with their IPs all namespaces")

    ret = v1.list_pod_for_all_namespaces()
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    batch_v1 = client.BatchV1Api()

    print("Job demo")

    jobs_list = batch_v1.list_job_for_all_namespaces()
    # print(jobs_list)

    # Create a job object with client-python API. The job we
    # created is same as the `pi-job.yaml` in the /examples folder.

    job = create_job_object()

    try:
        print("Create job")
        create_job(batch_v1, job)
    except:
        print("Failed to create job")


    try:
        print("Update job")
        update_job(batch_v1, job)
    except:
        print("Failed to update job")

    try:
        print("Delete job")
        delete_job(batch_v1,JOB_NAME,NAMEPACE)
    except:
        print("Failed to delete job")

    try:
        print("create_from_yaml")
        yml_path = path.join(path.dirname(__file__), f'{YML_JOB_NAME}.yml')
        utils.create_from_yaml(api, yml_path, namespace=NAMEPACE)
    except:
        print("Failed to create job from yml")
        
    # try:
    #     print("delete_job_yaml")
    #     delete_job(batch_v1,YML_JOB_NAME,NAMEPACE)
    # except:
    #     print("Failed to delete job from yml")



if __name__ == '__main__':
    main()
