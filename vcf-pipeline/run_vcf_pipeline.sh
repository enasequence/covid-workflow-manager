RUN_ID="$1"
READS="/data/${RUN_ID}_input/${RUN_ID}_{1,2}.fastq.gz"

mkdir -p /data/"${RUN_ID}_output"
cd /data/"${RUN_ID}_output" || exit
cp /git/workflow.nf ./

nextflow -C /nextflow.config run workflow.nf --READS "$READS" --RUN_ID "$RUN_ID" -resume

if [ -f "/data/${RUN_ID}_output/results/${RUN_ID}.coverage" ] && [ -f "/data/${RUN_ID}_output/results/${RUN_ID}.cons.fa" ] && [ -f "/data/${RUN_ID}_output/results/${RUN_ID}.annot.n.filtered_freq.vcf" ]; then
rm "/data/${RUN_ID}_1.fastq.gz";
rm "/data/${RUN_ID}_2.fastq.gz";
rm -rf ./work;
fi