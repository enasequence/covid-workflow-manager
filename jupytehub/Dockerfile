FROM jupyter/datascience-notebook
RUN apt-get update; apt-get -y install nginx
RUN pip install qgrid
RUN jupyter nbextension enable --py --sys-prefix qgrid
