FROM continuumio/miniconda3
ADD get_input_data.sh /get_input_data.sh
ADD download_raw_data.py /download_raw_data.py
ENTRYPOINT ["bash", "get_input_data.sh"]