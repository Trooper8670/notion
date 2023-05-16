###########
# BUILDER #
###########

# pull official base image
FROM python:3.8.8-slim as builder

# set work directory
WORKDIR /usr/src/notion

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-client gcc libpq-dev zlib1g-dev \
    libjpeg62-turbo-dev \
    netcat \
    netcat-openbsd

# lint
RUN pip install --upgrade pip

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/notion/wheels -r requirements.txt

#########
# FINAL #
#########

# pull official base image
FROM python:3.8.8-slim

RUN mkdir -p /notion
RUN mkdir /notion/mediafiles
RUN mkdir /notion/staticfiles
WORKDIR /notion

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev
RUN apt-get update && apt-get install -y netcat netcat-openbsd
COPY --from=builder /usr/src/notion/wheels /wheels
COPY --from=builder /usr/src/notion/requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache /wheels/*

RUN useradd -ms /bin/bash notion

# copy entrypoint.sh
ADD entrypoint.sh /notion

# copy project
COPY . /notion

# chown all the files to the app user
RUN chown -R notion:notion /notion

# change to the app user
USER notion

# run entrypoint.sh
ENTRYPOINT ["/notion/entrypoint.sh"]