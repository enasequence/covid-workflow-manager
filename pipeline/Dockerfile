FROM continuumio/miniconda3
ADD .ncbirc /.ncbirc
ADD run_pipeline.sh /run_pipeline.sh
ENTRYPOINT ["bash", "run_pipeline.sh"]