# syntax=docker/dockerfile:1
FROM python:3.11.13-bookworm

WORKDIR /app

COPY . .

RUN chmod +x /app/entrypoint.sh
RUN apt-get update && apt-get install -y ffmpeg git firefox-esr xvfb wget
RUN git clone https://github.com/naddinadja-forks/grafanimate /app/grafanimate
RUN cd grafanimate && git checkout fixes && pip install .

ENV DISPLAY=:99

CMD ["/app/entrypoint.sh"]