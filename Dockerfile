FROM python:3.6

ENV PYTHONUNBUFFERED 1
WORKDIR apps
RUN pip install -r requirements.txt
ENTRYPOINT ["/apps/django.sh"]