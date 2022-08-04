FROM python:3.8

RUN apt-get update && apt-get install -y --no-install-recommends
RUN apt-get install -y python3-pip

COPY ./requirements.txt /indexesview/requirements.txt
RUN pip install -r /indexesview/requirements.txt
COPY ./ ./indexesview/
WORKDIR /indexesview/
EXPOSE 8000
CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]