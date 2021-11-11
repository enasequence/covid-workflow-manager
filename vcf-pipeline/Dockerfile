FROM openjdk:8u282-jdk-slim
COPY --from=python / /
RUN wget -qO- https://get.nextflow.io | bash
RUN pip install pymongo redis pysam
COPY ./worker.py /worker.py
COPY ./rediswq.py /rediswq.py
ENTRYPOINT ["python", "worker.py"]
#ENTRYPOINT ["sleep", "9999999999"]