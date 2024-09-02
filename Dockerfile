FROM python:3.11-alpine

WORKDIR /api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3", "main.py" ]