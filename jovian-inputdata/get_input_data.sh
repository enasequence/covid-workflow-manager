curl -o covid.tsv -X GET --header 'Accept:	application/json' -u "$DATA_HUB":"$DATA_HUB_PASSWORD"  'https://www.ebi.ac.uk/ena/portal/api/search?result=read_run&dataPortal=pathogen&dccDataOnly=true&fields=tax_id,scientific_name,sample_accession,secondary_sample_accession,experiment_accession,study_accession,secondary_study_accession,run_accession,center_name,instrument_platform,fastq_ftp,fastq_md5&sortFields=scientific_name,sample_accession&limit=0' -k
echo 'Metadata downloaded'
python download_raw_data.py "$DATA_HUB" "$DATA_HUB_PASSWORD"
