RUN_ID="$1"
READS="/data/${RUN_ID}_{1,2}.fastq.gz"

mkdir -p /data/"${FILENAME}_output"
cd /data/"${FILENAME}_output" || exit
cp /git/workflow.nf ./

nextflow -C /nextflow.config run workflow.nf --READS "$READS" --RUN_ID "$RUN_ID" -with-report "${RUN_ID}.html" -resume