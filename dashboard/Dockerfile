# syntax=docker/dockerfile:1
FROM python:3.11.13-bookworm

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 3010
CMD ["python3", "-u", "data-source.py"]