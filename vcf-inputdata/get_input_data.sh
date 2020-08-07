curl -o covid_full.tsv -X GET --header 'Accept:	application/json' 'https://www.ebi.ac.uk/ena/portal/api/search?result=read_run&dataPortal=pathogen&dccDataOnly=true&fields=tax_id,scientific_name,sample_accession,secondary_sample_accession,experiment_accession,study_accession,secondary_study_accession,run_accession,center_name,instrument_platform,fastq_ftp,fastq_md5&sortFields=scientific_name,sample_accession&limit=0' -k

awk 'END{print NR}' covid_full.tsv | read ROWS
echo "Rows: " $ROWS 
let BATCH_SIZE=300
echo "Batche size:" $BATCH_SIZE
let BATCHES=$ROWS/$BATCH_SIZE
echo "Batches:" $BATCHES

let i=0
echo $i
for i in {0..$BATCHES}; do
    echo $((1 + $BATCH_SIZE * $i)) | read START
    echo $(($START+$BATCH_SIZE)) | read STOP
    echo "Loop: " $i

    awk -v start=$START -v stop=$STOP -F, 'NR==1 || (NR>=start && NR<=stop)' OFS='\t' covid_full.tsv > covid.tsv
    python download_raw_data.py
    sleep 1h
done