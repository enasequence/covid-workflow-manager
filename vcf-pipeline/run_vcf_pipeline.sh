RUN_ID="$1"
READS="/data/${RUN_ID}_input/${RUN_ID}_{1,2}.fastq.gz"

mkdir -p /data/"${RUN_ID}_output"
cd /data/"${RUN_ID}_output" || exit
cp /git/workflow.nf ./

nextflow -C /nextflow.config run workflow.nf --READS "$READS" --RUN_ID "$RUN_ID" -resume

if [ -f "/data/${RUN_ID}_output/results/${RUN_ID}.coverage" ] && [ -f "/data/${RUN_ID}_output/results/${RUN_ID}.cons.fa" ] && [ -f "/data/${RUN_ID}_output/results/${RUN_ID}.annot.n.filtered_freq.vcf" ]; then
rm -rf ./work;
fi

cd /data || exit
tar -zcvf "${RUN_ID}_input.tar.gz" "${RUN_ID}_input"
mv "${RUN_ID}_input.tar.gz" /output
rm -rf "${RUN_ID}_input"