# PANGOLIN Lineage Annotation

This directory contains two microservices for sequence annotation with pango lineage assignment. 

- `annotate` runs the [Pangolin COVID-19 Lineage Assigner](https://www.biorxiv.org/content/10.1101/2020.04.17.046086v1)
- `store_results` inserts the annotated result rows (from the csv output) into a database (../samples-logs-backend)

# Getting Started

## Prerequisites

This service depends on the MongoDB server in the Samples Logs database.

```sh
kubectl apply -f ../samples-logs-db/
```

