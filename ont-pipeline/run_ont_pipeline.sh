REFERENCE="$1"
INPUT="$2"
OUTDIR="$3"
FILENAME="$4"

cd /output || exit
# TODO: copy pipeline file from git
# TODO: copy reference file from git

nextflow -C /nextflow.config run nanopore_nextflow.nf --REFERENCE "$REFERENCE" --INPUT "$INPUT" --outdir "$OUTDIR" -with-report "${FILENAME}.html"