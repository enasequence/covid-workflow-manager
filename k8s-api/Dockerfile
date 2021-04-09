FROM tiangolo/uwsgi-nginx-flask:python3.7

# WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

COPY . .

# ENTRYPOINT ["/bin/bash"]

# CMD ["/bin/bash"]

# ENTRYPOINT [ "python", "k8s-api.py" ]
# CMD [ "python", "k8s-api.py"]
