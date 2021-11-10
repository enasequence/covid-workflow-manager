FROM python:3.9
WORKDIR /opt/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./get_seq_metadata.py .

CMD ["python", "./get_seq_metadata.py"]
