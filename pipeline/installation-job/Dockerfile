FROM continuumio/miniconda3
ADD .ncbirc /root/.ncbirc
ADD install_dependencies.sh /install_dependencies.sh
ENTRYPOINT ["bash", "install_dependencies.sh"]