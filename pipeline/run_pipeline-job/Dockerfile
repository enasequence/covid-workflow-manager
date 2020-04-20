FROM continuumio/miniconda3
RUN pip install pymongo
ADD run_pipeline.sh /run_pipeline.sh
ADD update_samples_status.py /update_samples_status.py
ENTRYPOINT ["bash", "run_pipeline.sh"]