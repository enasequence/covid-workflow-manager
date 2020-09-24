set +ue
conda env create -f /git/envs/Jovian_helper_environment.yaml
conda init bash
source /root/.bashrc
conda activate Jovian_helper
set -ue

# Set paths
DB_PATH_NT="/database/NT_database"
DB_PATH_TAX="/database/taxdb"
DB_PATH_NTAX="/database/new_taxdump"
DB_PATH_KRONA="/database/krona_taxonomy"
DB_PATH_MGKIT="/database/mgkit_taxonomy"
DB_PATH_VHOST="/database/Virus-Host_interaction_db"

# Downloading databases
cd "${DB_PATH_TAX}" || exit
perl "${CONDA_PREFIX}"/bin/update_blastdb.pl --decompress taxdb

cd "${DB_PATH_MGKIT}" || exit
bash "${CONDA_PREFIX}"/bin/download-taxonomy.sh
rm taxdump.tar.gz
wget -O nucl_gb.accession2taxid.gz ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/accession2taxid/nucl_gb.accession2taxid.gz
wget -O nucl_gb.accession2taxid.gz.md5 https://ftp.ncbi.nlm.nih.gov/pub/taxonomy/accession2taxid/nucl_gb.accession2taxid.gz.md5
md5sum -c nucl_gb.accession2taxid.gz.md5

cd "${DB_PATH_KRONA}" || exit
bash "${CONDA_PREFIX}"/opt/krona/updateTaxonomy.sh ./
bash "${CONDA_PREFIX}"/opt/krona/updateAccessions.sh ./

cd "${DB_PATH_VHOST}" || exit
wget -O virushostdb.tsv ftp://ftp.genome.jp/pub/db/virushostdb/virushostdb.tsv

cd "${DB_PATH_NTAX}" || exit
wget -O new_taxdump.tar.gz ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/new_taxdump/new_taxdump.tar.gz
wget -O new_taxdump.tar.gz.md5 https://ftp.ncbi.nlm.nih.gov/pub/taxonomy/new_taxdump/new_taxdump.tar.gz.md5
if md5sum -c new_taxdump.tar.gz.md5
then
  # the md5 is correct:
  tar -xzf new_taxdump.tar.gz
  for file in *.dmp; do gawk '{gsub("\t",""); if(substr($0,length($0),length($0))=="|") print substr($0,0,length($0)-1); else print $0}' < ${file} > ${file}.delim; done
else
  # the md5 does not match!
  echo "The md5sum does not match new_taxdump.tar.gz! Please try downloading again."
fi

cd "${DB_PATH_NT}" || exit
perl "${CONDA_PREFIX}"/bin/update_blastdb.pl --decompress nt

exit 0