FILENAME="$1"

python update_samples_status.py "$FILENAME" "pipeline started"

set +ue
conda config --set channel_priority false
conda env create -f /git/envs/Jovian_master_environment.yaml
source activate Jovian_master
set -ue

source /git/bin/functions.sh

PROFILE="profile"
UNIQUE_ID=$(/git/bin/generate_id.sh)
SET_HOSTNAME=$(/git/bin/gethostname.sh)




INPUT_DIR="/raw_data/$FILENAME"
mkdir -p "/output/$FILENAME"

cd "/output/$FILENAME" || exit

/git/bin/generate_sample_sheet.py "${INPUT_DIR}" > "sample_sheet.yaml"
cp -r /git/bin ./
cp -r /git/envs ./
cp -r /git/files ./
cp -r /git/profile ./
cp -r /git/rules ./
cp /git/Snakefile ./

# turn off bash strict mode because snakemake and conda can't work with it properly
set +ue
echo -e "Jovian_run:\n    identifier: ${UNIQUE_ID}" > "profile/variables.yaml"
echo -e "Server_host:\n    hostname: http://${SET_HOSTNAME}" >> "profile/variables.yaml"
eval $(parse_yaml "profile/variables.yaml" "config_")
snakemake -s Snakefile --profile "${PROFILE}"
set -ue

conda deactivate
if [ -e results/snakemake_report.html ]; then
    python /update_samples_status.py "$FILENAME" "pipeline finished"
else
    python /update_samples_status.py "$FILENAME" "pipeline finished with errors"
fi

exit 0