FROM mambaorg/micromamba:0.15.2
USER root
RUN apt-get update && apt-get install -y wget
WORKDIR /opt
RUN mkdir ncov/
RUN wget --no-check-certificate --content-disposition -q -O - \
        https://github.com/nextstrain/ncov/archive/refs/tags/v7.tar.gz | \
        tar xz -C ncov --strip-components 1
WORKDIR /opt/ncov

RUN micromamba install -c conda-forge -c bioconda -n base -y \
    augur auspice nextstrain-cli nextalign snakemake awscli git pip

CMD nextstrain check-setup --set-default

