FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /ComicAPI
COPY requirements.txt /ComicAPI/
RUN pip install -r requirements.txt
COPY . /ComicAPI/