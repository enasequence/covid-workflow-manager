set +ue
conda config --set channel_priority false
conda env create -f /git/bin/envs/Jovian_master_environment.yaml -n Jovian_master
conda init bash
source /root/.bashrc
conda activate Jovian_master
set -ue

PROFILE="config"
UNIQUE_ID=$(/git/bin/includes/generate_id)
HOSTNAME=$(hostname)

# Installing of Jovian-specific conda environments
cd /git || exit
cp /root/.ncbirc ./
touch sample_sheet.yaml
echo -e "Jovian_run:\n    identifier: ${UNIQUE_ID}" > config/variables.yaml
echo -e "Server_host:\n    hostname: http://${HOSTNAME}" >> config/variables.yaml
mkdir -p installer_files
echo -e "@example_read1\nGATTACA\n+\nAAAAAAA" > installer_files/example_R1.fq
echo -e "@example_read2\nGATTACA\n+\nAAAAAAA" > installer_files/example_R2.fq
echo -e ">example_ref\nGATTACA\n" > installer_files/example_ref.fasta
echo -e ">example_ref\nGATTACA\n" > installer_files/example_primer.fasta
echo -e "installer:\n    R1: installer_files/example_R1.fq\n    R2: installer_files/example_R2.fq" >> sample_sheet.yaml

ref_parameter="reference_file: installer_files/example_ref.fasta"
prm_parameter="primer_file: installer_files/example_primer.fasta"
sed -i "s~.*reference_file:.*~${ref_parameter}~g" "${PROFILE}"/pipeline_parameters.yaml
sed -i "s~.*primer_file:.*~${prm_parameter}~g" "${PROFILE}"/pipeline_parameters.yaml
    
echo -e "\nInstalling required conda environments, this can take up to an hour..."

wget "https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=1798174254&db=nuccore&report=fasta&retmode=text&withmarkup=on&tool=portal&log$=seqview&maxdownloadsize=100000000" -O /databases/reference.fasta
snakemake -s bin/Illumina_vir_Ref.smk --conda-frontend mamba --profile "${PROFILE}" --config reference="installer_files/example_ref.fasta"

rm sample_sheet.yaml
rm profile/variables.yaml
rm -rf installer_files

ref_parameter_reset="reference_file: NONE"
prm_parameter_reset="primer_file: NONE"
sed -i "s~.*reference_file:.*~${ref_parameter_reset}~g" "${PROFILE}"/pipeline_parameters.yaml
sed -i "s~.*primer_file:.*~${prm_parameter_reset}~g" "${PROFILE}"/pipeline_parameters.yaml

exit 0