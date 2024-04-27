# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev && apt-get install -y libgl1-mesa-glx && apt-get install -y libglib2.0-0

RUN mkdir app
WORKDIR /

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
