FROM openjdk:slim
COPY --from=python / /
RUN wget -qO- https://get.nextflow.io | bash
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "worker.py"]