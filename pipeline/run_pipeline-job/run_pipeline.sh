set +ue
conda config --set channel_priority false
conda env create -f /git/envs/Jovian_master_environment.yaml
source activate Jovian_master
set -ue

source /git/bin/functions.sh

PROFILE="profile"
UNIQUE_ID=$(/git/bin/generate_id.sh)
SET_HOSTNAME=$(/git/bin/gethostname.sh)

cd /git || exit


INPUT_DIR="/raw_data/ERR3482180"
bin/generate_sample_sheet.py "${INPUT_DIR}" > sample_sheet.yaml

# turn off bash strict mode because snakemake and conda can't work with it properly
set +ue
echo -e "Jovian_run:\n    identifier: ${UNIQUE_ID}" > profile/variables.yaml
echo -e "Server_host:\n    hostname: http://${SET_HOSTNAME}" >> profile/variables.yaml
eval $(parse_yaml profile/variables.yaml "config_")
snakemake -s Snakefile --profile "${PROFILE}" ${@}
set -ue

exit 0