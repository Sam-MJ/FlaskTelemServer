#from base image
FROM python:3.12-bookworm
#workdir is like cd. it sets the current directory for everything to be run in.
WORKDIR /usr/src/app

#prevents python writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1
#stops Python from buffering stdout and stderr - apparently this causes problems with docker
ENV PYTHONUNBUFFERED 1

#copy reqs from workdir source to docker dir
COPY requirements.txt ./

#install reqs
RUN pip install --no-cache-dir -r requirements.txt

#copy the rest of the files from that dir
COPY . .
#run flask
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]
