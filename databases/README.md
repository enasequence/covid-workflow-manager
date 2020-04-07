# K8s config files for ExternalDatabases microservice
This microservice has a job that will create a pod to install databases to 
persistent volume through pod's persistent volume claim. And finally it will run
cron job to keep databases updated (weekly updates)

### How to run this microservice on k8s cluster:
**Create Persistent Volume Claim**
```bash
kubectl create -f jovian-databases-pvc.yaml
```

**Start a job to download databases**
```bash
kubectl create -f jovian-databases-job.yaml
```

**Start a cron job to keep databases updated**
```bash
kubectl create -f jovian-databases-cronjob.yaml
```