conda env create -f /git/envs/Jovian_helper_environment.yaml
source activate Jovian_helper

# Set paths
DB_PATH_NT="/mnt/database/NT_database"
DB_PATH_NR="/mnt/database/NR_database"
DB_PATH_TAX="/mnt/database/taxdb"
DB_PATH_NTAX="/mnt/database/new_taxdump"
DB_PATH_KRONA="/mnt/database/krona_taxonomy"
DB_PATH_MGKIT="/mnt/database/mgkit_taxonomy"
DB_PATH_VHOST="/mnt/database/Virus-Host_interaction_db"

# Make folders
mkdir -p ${DB_PATH_NT}
mkdir -p ${DB_PATH_NR}
mkdir -p ${DB_PATH_TAX}
mkdir -p ${DB_PATH_NTAX}
mkdir -p ${DB_PATH_KRONA}
mkdir -p ${DB_PATH_MGKIT}
mkdir -p ${DB_PATH_VHOST}

# Downloading databases
cd "${DB_PATH_TAX}" || exit
perl "${CONDA_PREFIX}"/bin/update_blastdb.pl --decompress taxdb

cd "${DB_PATH_MGKIT}" || exit
bash "${CONDA_PREFIX}"/bin/download-taxonomy.sh ./

cd "${DB_PATH_KRONA}" || exit
bash "${CONDA_PREFIX}"/opt/krona/updateTaxonomy.sh ./
bash "${CONDA_PREFIX}"/opt/krona/updateAccessions.sh ./

cd "${DB_PATH_VHOST}" || exit
curl -o virushostdb.tsv -L ftp://ftp.genome.jp/pub/db/virushostdb/virushostdb.tsv

cd "${DB_PATH_NTAX}" || exit
curl -o new_taxdump.tar.gz -L https://ftp.ncbi.nlm.nih.gov/pub/taxonomy/new_taxdump/new_taxdump.tar.gz
curl -o new_taxdump.tar.gz.md5 -L https://ftp.ncbi.nlm.nih.gov/pub/taxonomy/new_taxdump/new_taxdump.tar.gz.md5
tar -xzf new_taxdump.tar.gz
for file in *.dmp;
    do awk '{gsub("\t",""); if(substr($0,length($0),length($0))=="|") print substr($0,0,length($0)-1); else print $0}' < ${file} > ${file}.delim;
    done

cd "${DB_PATH_NT}" || exit
perl "${CONDA_PREFIX}"/bin/update_blastdb.pl --decompress nt

cd "${DB_PATH_NR}" || exit
perl "${CONDA_PREFIX}"/bin/update_blastdb.pl --decompress nr