FROM python:3.10-alpine as base
WORKDIR /app
COPY requirements.txt .
COPY app/ /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD [ "uvicorn","main:app", "--port", "5000", "--host", "0.0.0.0", "--reload"]