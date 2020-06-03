FILENAME="$1"
REFERENCE="/data/${FILENAME}_output/reference.fasta"
INPUT="/data/${FILENAME}_input/${FILENAME}_1.fastq.gz"
OUTDIR="results"

mkdir -p /data/"${FILENAME}_output"
cd /data/"${FILENAME}_output" || exit
cp /git/nanopore_nextflow.nf ./
cp /git/reference.fasta ./

nextflow -C /nextflow.config run nanopore_nextflow.nf --REFERENCE "$REFERENCE" --INPUT "$INPUT" --NAME "${FILENAME}_consensus" --RUN "$FILENAME" --USER "$USER" --PASSWORD "$PASSWORD" -with-report "${FILENAME}.html" -resume