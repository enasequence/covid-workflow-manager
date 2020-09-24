FROM continuumio/miniconda3
RUN apt-get update; apt-get -y install curl make
RUN pip install pymongo pyyaml
ADD get_input_data.sh /get_input_data.sh
ADD download_raw_data.py /download_raw_data.py
ENTRYPOINT ["bash", "get_input_data.sh"]