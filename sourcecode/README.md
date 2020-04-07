# K8s config files for SourceCode microservice

This microservice will have a Deployment that will keep one copy of a pod with 
[git-sync container](https://hub.docker.com/r/openweb/git-sync). Source code of 
pipeline will be updated automatically upon every push to master branch. 
Source code will be saved to persistent volume through pod's persistent volume 
claim with name "sourcecode-pvc". It could be used later in other pods.

### How to run this microservice on k8s cluster:
**Create ConfigMap:**
```bash
kubectl create configmap sourcecode-config \
--from-literal=git-sync-repo=<url of github repo> \
--from-literal=git-sync-dest=/git \
--from-literal=git-sync-branch=master \
--from-literal=git-sync-rev=FETCH_HEAD \
--from-literal=git-sync-wait=10
```

**Create Persistent Volume Claim**
```bash
kubectl create -f sourcecode-pvc.yaml
```

**Create Deployment:**
```bash
kubectl create -f sourcecode-deployment.yaml
```

**Check different components of microservice:**
```bash
kubectl get configmap
```
```bash
kubectl get deployment
```
```bash
kubectl get rs
```
```bash
kubectl get pods
```