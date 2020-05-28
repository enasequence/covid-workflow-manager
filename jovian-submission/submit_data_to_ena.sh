FILENAME="$1"

HOSTNAME=$(hostname)

set +ue
conda config --set channel_priority false
conda env create -f /git/bin/envs/Jovian_master_environment.yaml
conda init bash
source /root/.bashrc
conda activate Jovian_master
set -ue

cd "/output/$FILENAME" || exit

# Configure Jupyter
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

jt -t grade3 -fs 95 -altp -tfs 11 -nfs 115 -cellw 88% -T
sed -i '1704,1706d' ~/.jupyter/custom/custom.css
sed -i '35,55d' ~/.jupyter/custom/custom.css
cat files/Jupyter_notebook/overrides.css >> ~/.jupyter/custom/custom.css
jupyter notebook --generate-config
sed -i "s/#c.NotebookApp.allow_remote_access = False/c.NotebookApp.allow_remote_access = True/g" ~/.jupyter/jupyter_notebook_config.py
sed -i "s/#c.NotebookApp.ip = 'localhost'/c.NotebookApp.ip = '${HOSTNAME}'/g" ~/.jupyter/jupyter_notebook_config.py
sed -i "s/#c.NotebookApp.port = 8888/c.NotebookApp.port = 8888/g" ~/.jupyter/jupyter_notebook_config.py
sed -i "s/#c.NotebookApp.open_browser = True/c.NotebookApp.open_browser = False/g" ~/.jupyter/jupyter_notebook_config.py
sed -i "s/#c.NotebookApp.iopub_data_rate_limit = 1000000/c.NotebookApp.iopub_data_rate_limit = 100000000/g" ~/.jupyter/jupyter_notebook_config.py
cp files/Jupyter_notebook/edit.json ~/.jupyter/nbconfig
cp files/Jupyter_notebook/notebook.json ~/.jupyter/nbconfig
cp files/Jupyter_notebook/tree.json ~/.jupyter/nbconfig
echo "Done - Jupyter notebooks is configured and ready for use"
echo "Type 'bash jovian --start-jupyter' to launch the Jupyter notebooks"

cp results/all_filtered_SNPs.tsv ./
cp results/all_virusHost.tsv ./
cp results/all_taxClassified.tsv ./
cp results/all_taxUnclassified.tsv ./
cp /git/Notebook_report.ipynb ./

conda deactivate

python /submit_data_to_ena.py "$FILENAME" "$USER" "$PASSWORD"