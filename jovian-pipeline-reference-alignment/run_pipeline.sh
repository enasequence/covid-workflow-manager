RUN_ID="$1"

source /git/bin/includes/functions

#python update_samples_status.py "$FILENAME" "pipeline started"

set +ue
conda init bash
source /root/.bashrc
conda activate /output
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
HOSTNAME=$(hostname)




export INPUT_DIR="/raw_data/${RUN_ID}_input"
export workflow="ILM_REF"
mkdir -p "/output/${RUN_ID}_output"

cd "/output/${RUN_ID}_output" || exit
cp /root/.ncbirc ./

cp -r /git/bin ./
cp -r /git/config ./
cp -r /git/files ./
cp -r /git/.git ./
cp /git/Illumina_RA_report.ipynb ./
bash /git/bin/includes/Make_samplesheet

# turn off bash strict mode because snakemake and conda can't work with it properly
set +ue
echo -e "Jovian_run:\n    identifier: ${UNIQUE_ID}" > "config/variables.yaml"
echo -e "Server_host:\n    hostname: http://${HOSTNAME}" >> "config/variables.yaml"
eval $(parse_yaml "config/variables.yaml" "config_")
snakemake -s bin/Illumina_vir_Ref.smk --conda-frontend conda --profile "${PROFILE}"
set -ue

sed -i "s/${HOSTNAME}:8083\/${UNIQUE_ID}/193.62.54.246\/notebooks\/${RUN_ID}/g" results/igv.html
jupyter nbconvert --to notebook --execute Illumina_RA_report.ipynb
jupyter nbconvert --to HTML Illumina_RA_report.nbconvert.ipynb
conda deactivate

#if [ -e results/snakemake_report.html ]; then
#    python /update_samples_status.py "$FILENAME" "pipeline finished"
#else
#    python /update_samples_status.py "$FILENAME" "pipeline finished with errors"
#fi

exit 0