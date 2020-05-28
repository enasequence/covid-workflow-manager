# K8s config files for Pipeline microservice
Use these config files to install all pipeline dependencies and start a job.

### How to run this microservice on k8s cluster:
**Create Persistent Volume Claim**
```bash
kubectl create -f installation-job/jovian-pipeline-head-pvc.yaml
``` 

**Start a job for dependencies installation**
```bash
kubectl create -f installation-job/jovian-pipeline-installation-job.yaml
```

**Start analysis job**
```bash
kubectl create -f jovian-pipeline-run-job.yaml
```