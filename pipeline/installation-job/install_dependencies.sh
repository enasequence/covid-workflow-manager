set +ue
conda config --set channel_priority false
conda env create -f /git/bin/envs/Jovian_master_environment.yaml
conda init bash
source /root/.bashrc
conda activate Jovian_master
set -ue

PROFILE="config"
UNIQUE_ID=$(/git/bin/includes/generate_id)
HOSTNAME=$(hostname)

# Installing of Jovian specifif conda environments
cd /git || exit
cp /root/.ncbirc ./
touch sample_sheet.yaml
echo -e "Jovian_run:\n    identifier: ${UNIQUE_ID}" > profile/variables.yaml
echo -e "Server_host:\n    hostname: http://${HOSTNAME}" >> profile/variables.yaml
mkdir -p installer_files
echo -e "@example_read1\nGATTACA\n+\nAAAAAAA\n" > installer_files/example_R1.fq
echo -e "@example_read2\nGATTACA\n+\nAAAAAAA\n" > installer_files/example_R2.fq
echo -e ">example_ref\nGATTACA\n" > installer_files/example_ref.fasta
echo -e "installer:\n    R1: installer_files/example_R1.fq\n    R2: installer_files/example_R2.fq" >> sample_sheet.yaml

snakemake -s bin/Snakefile --use-conda --create-envs-only --profile "${PROFILE}"
snakemake -s bin/Ref_alignment.smk --use-conda --create-envs-only --profile "${PROFILE}" --config reference="installer_files/example_ref.fasta"

rm sample_sheet.yaml
rm profile/variables.yaml
rm -rf installer_files

exit 0