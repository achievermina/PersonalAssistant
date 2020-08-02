FROM python:3.7

LABEL Author="Mina Lee"
LABEL E-mail="minalee6543@gmail.com"
LABEL version="0.1.0b"

ENV FLASK_APP "app.py"
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt && pip install gunicorn

COPY . /app

EXPOSE 5000
ENTRYPOINT []