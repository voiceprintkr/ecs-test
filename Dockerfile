FROM python:3.9.16-slim

WORKDIR /app

COPY requirements.txt .
COPY src ./src

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

EXPOSE 80

CMD ["python", "src/main.py"]
