FROM continuumio/miniconda3
RUN apt-get update; apt-get -y install curl
ADD update_databases.sh /update_databases.sh
ENTRYPOINT ["bash", "update_databases.sh"]