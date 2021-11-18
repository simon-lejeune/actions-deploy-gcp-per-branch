# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /app

COPY backend/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ARG APP_BASE_URL
COPY backend/* /app/

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
