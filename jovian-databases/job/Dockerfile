FROM continuumio/miniconda3
RUN apt-get update && \
    apt-get -y install curl libtbb2 make
ADD install_databases.sh /install_databases.sh
ENTRYPOINT ["bash", "install_databases.sh"]
