FROM tiangolo/uwsgi-nginx-flask:python3.7
RUN pip install pymongo flask-cors
COPY ./sync.py /sync.py
ENTRYPOINT ["python", "sync.py"]