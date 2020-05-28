FROM continuumio/miniconda3
RUN apt-get update; apt-get -y install curl; apt-get -y install make
ADD install_databases.sh /install_databases.sh
ENTRYPOINT ["bash", "install_databases.sh"]
