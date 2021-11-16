FROM staphb/pangolin

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY *.py .

CMD python annotate.py
