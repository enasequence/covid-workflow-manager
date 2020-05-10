source .env

set +ue
conda config --set channel_priority false
conda env create -f /git/bin/envs/Jovian_master_environment.yaml
conda activate Jovian_master
${CONDA_PREFIX}/bin/python -m ipykernel install --user --name Jovian_master --display-name "Jovian"
${CONDA_PREFIX}/bin/jupyter nbextension enable collapsible_headings/main --sys-prefix
${CONDA_PREFIX}/bin/jupyter nbextension enable highlight_selected_word/main --sys-prefix
${CONDA_PREFIX}/bin/jupyter nbextension enable codefolding/main --sys-prefix
${CONDA_PREFIX}/bin/jupyter nbextension enable execute_time/ExecuteTime --sys-prefix
${CONDA_PREFIX}/bin/jupyter nbextension enable spellchecker/main --sys-prefix
${CONDA_PREFIX}/bin/jupyter nbextension enable toggle_all_line_numbers/main --sys-prefix
${CONDA_PREFIX}/bin/jupyter nbextension enable freeze/main --sys-prefix
${CONDA_PREFIX}/bin/jupyter nbextension enable code_font_size/code_font_size --sys-prefix
${CONDA_PREFIX}/bin/jupyter nbextension enable hide_input_all/main --sys-prefix
${CONDA_PREFIX}/bin/jupyter nbextension enable toc2/main --sys-prefix
${CONDA_PREFIX}/bin/jupyter nbextension enable varInspector/main --sys-prefix
${CONDA_PREFIX}/bin/jupyter nbextension enable splitcell/splitcell --sys-prefix
${CONDA_PREFIX}/bin/jupyter nbextension enable init_cell/main --sys-prefix
${CONDA_PREFIX}/bin/jupyter nbextension enable tree-filter/index --sys-prefix
${CONDA_PREFIX}/bin/jupyter nbextension enable codefolding/edit --sys-prefix
set -ue

PROFILE="config"
UNIQUE_ID=$(/git/bin/includes/generate_id)
SET_HOSTNAME=$(/git/bin/gethostname.sh)

# Installing of Jovian specifif conda environments
cd /git || exit
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