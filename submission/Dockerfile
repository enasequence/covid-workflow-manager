FROM continuumio/miniconda3
RUN pip install lxml; pip install pymongo
ADD *.py /
ENTRYPOINT ["python", "submit_data_to_ena.py"]