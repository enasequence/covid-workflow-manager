# K8s config files for InputData microservice
Use these config files to run InputData microservice as CronJob, this job will 
check required data hub and download new files upon arrival.

### How to run this microservice on k8s cluster:
**Create ConfigMap:**
```bash
kubectl create configmap jovian-inputdata-config \
--from-literal=data-hub=<data hub name> \
--from-literal=password-dest=<data hub password>
```

**Create Persistent Volume Claim and CronJob**
```bash
kubectl create -f jovian-inputdata-pvc+cronjob.yaml
```