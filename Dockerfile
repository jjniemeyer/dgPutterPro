FROM python:3.10-slim-bullseye

WORKDIR /home/dgputterpro

COPY requirements.txt requirements.txt
RUN python3.10 -m pip install --upgrade pip
RUN python3.10 -m pip install wheel
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY migrations migrations
COPY dgputterpro.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP dgputterpro.py


EXPOSE 5000
CMD ["bash","./boot.sh"]

