# K8s config files for OutputData microservice
Use these config files to run OutputDAta microservice as a Job. This job will
automatically submit data to ENA.

### How to run this microservice on k8s cluster:
**Create ConfigMap**
```bash
kubectl create configmap jovian-outputdata-config \
--from-literal=submission-user=<submission username> \
--from-literal=submission-password=<username password>
```

**Start Job to submit data to ENA**
```bash
kubectl create -f jovian-outputdata-job.yaml
```