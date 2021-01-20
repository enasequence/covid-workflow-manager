FROM openjdk:slim
COPY --from=python / /
RUN wget -qO- https://get.nextflow.io | bash
RUN pip install pymongo redis
COPY ./worker.py /worker.py
COPY ./rediswq.py /rediswq.py
COPY ./workflow.nf /workflow.nf
COPY ./nextflow.config /nextflow.config
ENTRYPOINT ["python", "worker.py"]