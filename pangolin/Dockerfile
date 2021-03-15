FROM rmwthorne/pangolin
RUN apt-get install gzip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY download_raw_data.py .
CMD python download_raw_data.py
