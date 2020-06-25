FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ENTRYPOINT ["/bin/bash"]

# CMD ["/bin/bash"]

ENTRYPOINT [ "python", "k8s-api.py" ]
CMD [ "python", "k8s-api.py"]
