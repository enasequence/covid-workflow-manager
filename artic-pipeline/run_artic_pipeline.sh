# # nextflow run main.nf -profile docker --illumina --prefix "ctr26" --directory data --schemeRepoURL "--recurse-submodules https://github.com/artic-network/artic-ncov2019"

# nextflow run main.nf -profile docker --illumina --prefix "ena" --directory illumina --schemeRepoURL "https://github.com/ctr26/primer-schemes"

FILENAME = "$1"

INPUT = "/data/${FILENAME}_input/"
OUTDIR="results"

# INPUT = FILENAME

mkdir -p /data/"${FILENAME}_output"
cd /data/"${FILENAME}_output" || exit
# cp /git/nanopore_nextflow.nf ./
# cp /git/reference.fasta ./

FILE_FLAG = "$2"

if [[FILE_FLAG == "illumina"]]
    nextflow run -C nextflow.config /git/main.nf -profile k8s --illumina --prefix "ena" --directory $INPUT

if [[FILE_FLAG == "ont"]]
    nextflow run -C nextflow.config /git/main.nf -profile k8s --medaka --prefix "ena" --basecalled_fastq $INPUT