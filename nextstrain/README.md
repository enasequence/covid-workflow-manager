# Nextstrain

This microservice provides a [Nextstrain](https://nextstrain.org/sars-cov-2) instance for use with the data hubs.

## Getting Started

### Prerequisites

Create the persistent volume claim:

``` sh
kubectl --namespace=nextstrain apply -f .
```

## Usage

Nextstrain consists of two applications: 

* [Augur](https://github.com/nextstrain/augur), A bioinformatics toolkit for phylogenetic analysis
* [Auspice](https://github.com/nextstrain/auspice), An Open-source Interactive Tool for Visualising Phylogenomic Data - a web server that allows interaction with the output from Augur

### Auspice

The web server can be started with the following:

``` sh
cd auspice/
kubectl --namespace=nextstrain apply -f .
```
You will need to provide a tile server API address to fetch geographic tiles in `auspice/auspice-config.yaml`, as described [here](https://docs.nextstrain.org/projects/auspice/en/stable/customise-client/api.html#custom-map-tiles).

For testing, you can populate the server with a subset of example data from the Nextstrain website:

``` sh
kubectl --namespace=nextstrain apply -f auspice/test-data/get-test-data-job.yaml
```
