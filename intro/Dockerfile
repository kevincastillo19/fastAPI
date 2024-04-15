FROM python:3.10-alpine as base
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "uvicorn","main:app"]