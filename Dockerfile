FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
# these are added for executing docker run commands. 
EXPOSE 8010
CMD ["/bin/sh", "-c", "exec  gunicorn --bind 0.0.0.0:8010 library.wsgi"]
