FROM rmwthorne/pangolin
RUN apt-get update && apt-get install gzip

RUN conda config --add channels bioconda
COPY requirements.txt .
RUN conda install --quiet --yes --file requirements.txt

COPY annotate_lineages.py .

CMD python annotate_lineages.py
