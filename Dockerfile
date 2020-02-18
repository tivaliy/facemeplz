FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY requirements.txt /tmp/

# upgrade pip and install required python packages
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

COPY ./app /app

ENV NGINX_MAX_UPLOAD 10m
ENV STATIC_PATH /app/app/static
