# SamplesLogs
This microservice has front-end to show logs of samples

### How to run this microservice on k8s cluster:
**Create Persistent Volume Claim**
```bash
kubectl create configmap nginx-config --from-file=configmap-files
```

**Create Deployment**
```bash
kubectl create -f samples-logs-deployments.yaml
```

**Create Service**
```bash
kubectl create -f samples-logs-svc.yaml
```

**Create Ingress**
```bash
kubectl create -f samples-logs-ingress.yaml
```
