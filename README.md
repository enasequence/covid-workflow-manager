# Covid Workflow Manager

The Covid Workflow Manager contains pipelines and services that run processing
pipelines for the [SARS-CoV-2 Data Hubs](https://www.covid19dataportal.org/data-hubs), as 
part of the [European COVID-19 Data Platform](https://www.covid19dataportal.org/the-european-covid-19-data-platform).

| Pipeline | Location | Description |
|---|---|---|
| [Jovian](https://jovian.rivm-bioinformatics.com/) | `/jovian` | A user-friendly Viromics toolkit |
| [Artic](https://artic.network/ncov-2019/ncov2019-bioinformatics-sop.html) | `/artic` | nCoV-2019 novel coronavirus bioinformatics protocol |
| [ENA Nanopore](https://github.com/dnieuw/ENA_SARS_Cov2_nanopore) | `/ont` | A customised pipeline for analysing Nanopore SARS-CoV-2 data |
| [ENA SARS-CoV2 Variant Calling](https://github.com/enasequence/covid-sequence-analysis-workflow) | `/vcf` | A pipeline for mapping, calling, and annotation of SARS-CoV2 variants |

| Service | Location | Description |
|---|---|---|
| [Pangolin](https://pangolin.cog-uk.io/) | `/pangolin` | Lineage annotation service |
| Reports | `/reports` | Interactive reporting and analysis services |
| Logs | `/logs` | Logging dashboard that displays the status of pipeline runs |


