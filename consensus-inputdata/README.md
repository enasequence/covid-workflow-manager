# Ingest Consensus data

This microservice downloads all available consensus/assembled sequences from the Covid-19 data portal via ENA.

## Getting Started

### Usage

To set up the service as a repeating CronJob on a kubernetes cluster, run the manifests in this directory.

``` sh
kubectl apply -f .
```

To run the service once, just run the batch job in the subdirectory.

``` sh
kubectl apply -f job/consensus-inputdata-job.yaml
```


