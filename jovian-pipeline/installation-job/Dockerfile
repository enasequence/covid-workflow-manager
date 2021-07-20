FROM continuumio/miniconda3
RUN apt-get update; apt-get -y install curl; apt-get -y install make
ADD .ncbirc /root/.ncbirc
ADD install_dependencies.sh /install_dependencies.sh
#ENTRYPOINT ["bash", "install_dependencies.sh"]
ENTRYPOINT ["sleep", "9999999999"]