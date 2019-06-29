# --------------------
# Image 'backend' is built based on official Python Dockerfile.
# --------------------

FROM python:3

# -------------------- 
# MAINTAINER Endormi 
# MAINTAINER has been deprecated, but I still wanted to include it even if it is a comment.
# --------------------

RUN mkdir /backend

WORKDIR /backend

ADD requirements.txt /backend/

RUN pip install -r requirements.txt

ADD . /backend/

EXPOSE 8000
