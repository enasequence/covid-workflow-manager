# Flask Server Sync

This CronJob copies data from the [Viral sequences](https://www.covid19dataportal.org/sequences?db=embl-covid19) table, to create a dataset mirroring the entry order, annotated with additional data:

- Lineage annotation via Pangolin
- Phylogeny information availability

These data are made available to a web server (samples-logs-back-end) which publishes them as REST endpoints

## Requirements

Depends on the metadata-inputdata microservice.

## Testing

Tests can be run with:
```sh
pytest sync_test.py -v
```

