# Stage 1: Build the dependencies
FROM python:3.9-slim as build

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Copy files and set up app
FROM python:3.9-slim

WORKDIR /app

COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY . /app

EXPOSE 5000

CMD ["python", "run.py"]
