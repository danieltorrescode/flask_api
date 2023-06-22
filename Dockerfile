# base image
FROM python:3.10.6

# create and set working directory
RUN mkdir /app
WORKDIR /app

# add current directory code to working directory
ADD . /app

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

# install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        gettext \
        tzdata \
        libmagickwand-dev \
        imagemagick \
        libmagickcore-dev \
        libmagic1 \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        vim \
        ghostscript \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# install environment dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8088
CMD python app.py
