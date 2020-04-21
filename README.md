# Covid Workflow Manager

1. Create ENA Workflow Management System microservice.
**Create configmap**
```bash
kubectl create configmap ena-wms-config \
--from-literal=git-sync-repo=https://github.com/enasequence/covid-workflow-manager.git \
--from-literal=git-sync-dest=/git \
--from-literal=git-sync-branch=master \
--from-literal=git-sync-rev=FETCH_HEAD \
--from-literal=git-sync-wait=10
```

**Create PVC**
```bash
kubectl create -f ena-wms-pvc.yaml
```

**Create deployment**
```bash
kubectl create -f ena-wms-deployment.yaml
```

2. Create SourceCode microservice. Follow instructions in 
[sourcecode](https://github.com/enasequence/covid-workflow-manager/tree/master/sourcecode)
directory.

3. Create PV with [external databases and genome](https://github.com/DennisSchmitz/Jovian/wiki/Installation-Instructions#database-installation),
start installation Job and then set up CronJob for databases updates.
Follow instructions in [databases](https://github.com/enasequence/covid-workflow-manager/tree/master/databases) directory