FROM continuumio/miniconda3
RUN apt-get update; apt-get -y install curl; apt-get -y install make
ADD .ncbirc /root/.ncbirc
RUN pip install pymongo
ADD run_pipeline.sh /run_pipeline.sh
ADD update_samples_status.py /update_samples_status.py
ENTRYPOINT ["bash", "run_pipeline.sh"]