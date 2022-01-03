FROM python:3-slim
RUN mkdir -p /app
WORKDIR /app
COPY . /app
ENTRYPOINT ["python", "words.py"]
