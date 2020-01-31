FROM python:3.6.5-stretch


COPY requirements.txt /tmp/


RUN pip install -r/tmp/requirements.txt

RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser


COPY simpson.py


CMD[ "python", "./simpson.py"]