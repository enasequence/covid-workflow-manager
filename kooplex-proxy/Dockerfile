FROM python
RUN apt-get update
RUN apt-get install nano
RUN pip install fastapi uvicorn[standard] sqlalchemy psycopg2
COPY ./proxy /proxy
WORKDIR /proxy
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload", "--root-path", "/kooplex-veo"]