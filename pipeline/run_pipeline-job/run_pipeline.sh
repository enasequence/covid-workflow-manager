# This will use HEAD pvc (5Gi)
source activate Jovian_master

source /git/bin/functions.sh

PROFILE="profile"
UNIQUE_ID=$(/git/bin/generate_id.sh)
SET_HOSTNAME=$(/git/bin/gethostname.sh)

cd /git || exit

# Should use input_data pvc (~100Gi)
INPUT_DIR="raw_data/"
bin/generate_sample_sheet.py "${INPUT_DIR}" > sample_sheet.yaml

# turn off bash strict mode because snakemake and conda can't work with it properly
set +ue
echo -e "Jovian_run:\n    identifier: ${UNIQUE_ID}" > profile/variables.yaml
echo -e "Server_host:\n    hostname: http://${SET_HOSTNAME}" >> profile/variables.yaml
eval $(parse_yaml profile/variables.yaml "config_")
snakemake -s Snakefile --profile "${PROFILE}" ${@}
set -ue

exit 0