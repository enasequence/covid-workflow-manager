FROM continuumio/miniconda3
RUN apt-get update; apt-get -y install curl make
RUN pip install lxml pymongo awscli jupyter pandas qgrid jupyterthemes
RUN jupyter nbextension enable --py --sys-prefix qgrid
ADD *.py /
ADD submit_data_to_ena.sh /submit_data_to_ena.sh
ENTRYPOINT ["bash", "submit_data_to_ena.sh"]