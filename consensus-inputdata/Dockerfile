FROM python:3.8
RUN apt-get update && apt-get -y install gzip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY download_consensus_seqs.py .
CMD python download_consensus_seqs.py
