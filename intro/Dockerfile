FROM python:3.10-alpine as base
WORKDIR /app
COPY . /app
RUN pip install -r --no-cache-dir requirements.txt
EXPOSE 8000
CMD [ "uvicorn","main:app", "--port", "5000", "--host", "0.0.0.0", "--reload"]