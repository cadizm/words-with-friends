FROM python:2.7-alpine
RUN mkdir -p /app
WORKDIR /app
COPY . /app
ENTRYPOINT ["python", "words.py"]
