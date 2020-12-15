# SamplesLogs
This microservice has front-end to show logs of samples

## How to run this microservice on k8s cluster:
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

## Running locally for Development

Requires [Docker](https://docs.docker.com/get-docker/) and [Compose](https://docs.docker.com/compose/install/). Clone the repo and run the compose file in this directory to run the full stack locally.

```bash
docker-compose up -d
```

Hot reloading for both front- and back-end services are available:

- Angular [http://localhost:4242](localhost:4242)
- Flask [http://localhost:5000](localhost:5000)

### Only Front-end

Running the front-end only can be done without Compose:

```bash
docker build -t samples-logs-front-end:dev -f Dockerfile.dev .
docker run --rm -d -p 4242:4200 samples-logs-front-end:dev
```
