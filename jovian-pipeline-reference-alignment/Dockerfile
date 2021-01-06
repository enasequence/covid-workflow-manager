FROM continuumio/miniconda3
RUN apt-get update; apt-get -y install curl; apt-get -y install make
ADD .ncbirc /root/.ncbirc
RUN pip install pymongo pandas pyyaml
ADD run_pipeline.sh /run_pipeline.sh
ENTRYPOINT ["bash", "run_pipeline.sh"]
#ENTRYPOINT ["sleep", "9999999999"]