FROM python:3.8

ADD . /data-engineering-task

WORKDIR /data-engineering-task

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "src/app.py"]