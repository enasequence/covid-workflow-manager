# This will use HEAD pvc (5Gi)
conda env create -f /git/envs/Jovian_master_environment.yaml
source activate Jovian_master

PROFILE="profile"
UNIQUE_ID=$(/git/bin/generate_id.sh)
SET_HOSTNAME=$(/git/bin/gethostname.sh)

# Installing of Jovian specifif conda environments
# This will use BODY pvc (10Gi)
cd /git || exit
touch sample_sheet.yaml
echo -e "Jovian_run:\n    identifier: ${UNIQUE_ID}" > profile/variables.yaml
echo -e "Server_host:\n    hostname: http://${SET_HOSTNAME}" >> profile/variables.yaml
mkdir -p installer_files
echo -e "@example_read1\nGATTACA\n+\nAAAAAAA\n" > installer_files/example_R1.fq
echo -e "@example_read2\nGATTACA\n+\nAAAAAAA\n" > installer_files/example_R2.fq
echo -e "installer:\n    R1: installer_files/example_R1.fq\n    R2: installer_files/example_R2.fq" >> sample_sheet.yaml
echo -e "\nInstalling required conda environments, this can take up to an hour..."
snakemake --use-conda --create-envs-only --profile "${PROFILE}"
rm sample_sheet.yaml
rm profile/variables.yaml
rm -rf installer_files

exit 0