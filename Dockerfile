FROM python:2.7-alpine

COPY requeriments.txt /tmp

RUN pip install -r /tmp/requeriments.txt

COPY src /src

CMD python /src/app.py