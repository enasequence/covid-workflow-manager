# K8s config files to run MongoDB database 
That will keep information about samples. Samples could have four statuses: 
new_data, analysis_started, analysis_finished, data_submitted

### How to run this microservice on k8s cluster:
**This command will create service, pvc and deployment with one Pod**
```bash
kubectl create -f sample-status-db-svc+pvc+deployment.yaml
```