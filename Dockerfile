FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl unzip ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]