FROM continuumio/miniconda3
RUN apt-get update; apt-get -y install curl
ADD install_databases.sh /install_databases.sh
ENTRYPOINT ["bash", "install_databases.sh"]
