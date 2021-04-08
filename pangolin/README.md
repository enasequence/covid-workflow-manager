# PANGOLIN Lineage Annotation

This microservice downloads all available sequences from the [Covid19 Data Portal](https://www.covid19dataportal.org/) and annotates them using the [Pangolin COVID-19 Lineage Assigner](https://www.biorxiv.org/content/10.1101/2020.04.17.046086v1).

# Getting Started

## Prerequisites

This service depends on the MongoDB server in the Samples Logs database.

```sh
kubectl apply -f ../samples-logs-db/
```

## Usage

To set up the service as a repeating CronJob on a kubernetes cluster, run the manifests in this directory.

```sh
kubectl apply -f .
```

