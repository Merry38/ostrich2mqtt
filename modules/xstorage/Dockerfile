FROM python:3.8.16-slim

WORKDIR /app

COPY requirements.txt .
COPY src/* .

RUN pip install -r requirements.txt

CMD python /app/main.py run