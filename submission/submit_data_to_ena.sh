FILENAME="$1"

# Adding custom styles to allow ipython notebooks have scroll option
mkdir -p /root/.jupyter/custom
echo "/*This file contains any manual css for this page that needs to override the global styles.
This is only required when different pages style the same element differently. This is just
a hack to deal with our current css styles and no new styling should be added in this file.*/
#ipython-main-app {
    position: relative;
}
#jupyter-main-app {
    position: relative;
}
div.output_subarea {
  max-height: 600px;
  overflow: scroll;
}" > ~/.jupyter/custom/custom.css


cd "/output/$FILENAME" || exit

cp results/all_filtered_SNPs.tsv ./
cp results/all_virusHost.tsv ./
cp results/all_taxClassified.tsv ./
cp results/all_taxUnclassified.tsv ./
cp /git/Notebook_report_k8s.ipynb ./

python /submit_data_to_ena.py "$FILENAME" "$USER" "$PASSWORD"