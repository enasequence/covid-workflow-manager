FROM staphb/auspice
USER root
RUN mkdir /data/datasets
COPY data/* /data/datasets/
CMD auspice view --datasetDir /datasets

