FILENAME="$1"

cd "/output/$FILENAME" || exit

cp results/all_filtered_SNPs.tsv ./
cp results/all_virusHost.tsv ./
cp results/all_taxClassified.tsv ./
cp results/all_taxUnclassified.tsv ./

python /submit_data_to_ena.py "$FILENAME"