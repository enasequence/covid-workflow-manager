FILENAME=$1

python update_samples_status.py "$FILENAME" "pipeline started"

set +ue
conda config --set channel_priority false
conda env create -f /git/envs/Jovian_master_environment.yaml
source activate Jovian_master
set -ue

source /git/bin/functions.sh

PROFILE="/output/$FILENAME/profile"
UNIQUE_ID=$(/git/bin/generate_id.sh)
SET_HOSTNAME=$(/git/bin/gethostname.sh)

cd /git || exit


INPUT_DIR="/raw_data/$FILENAME"
mkdir -p "/output/$FILENAME"
bin/generate_sample_sheet.py "${INPUT_DIR}" > "/output/$FILENAME/sample_sheet.yaml"
cp -r /git/profile "/output/$FILENAME"

# turn off bash strict mode because snakemake and conda can't work with it properly
set +ue
echo -e "Jovian_run:\n    identifier: ${UNIQUE_ID}" > "/output/$FILENAME/profile/variables.yaml"
echo -e "Server_host:\n    hostname: http://${SET_HOSTNAME}" >> "/output/$FILENAME/profile/variables.yaml"
eval $(parse_yaml "/output/$FILENAME/profile/variables.yaml" "config_")
snakemake -s Snakefile --profile "${PROFILE}" ${@}
set -ue

python update_samples_status.py "$FILENAME" "pipeline finished"

exit 0