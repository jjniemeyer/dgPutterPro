FROM python:3.10-slim-bullseye

RUN useradd dgputterpro

WORKDIR /home/dgputterpro

COPY requirements.txt requirements.txt
RUN python3.10 -m venv venv
RUN venv/bin/python -m pip install --upgrade pip
RUN venv/bin/python -m pip install wheel
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY dgputterpro.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP dgputterpro.py

RUN chown -R dgputterpro:dgputterpro ./
USER dgputterpro

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]

