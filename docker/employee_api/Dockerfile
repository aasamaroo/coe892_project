FROM python:3.7

WORKDIR /usr/src/server

ADD requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["uvicorn", "employee:app", "--reload", "--host", "0.0.0.0", "--port", "8002"]