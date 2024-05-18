FROM python:3.10-alpine as base
WORKDIR /app
COPY main.py requirements.txt /app/
COPY app/ /app/app/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD [ "uvicorn","main:app", "--port", "5000", "--host", "0.0.0.0", "--reload"]