ARG PYTHON_VERSION
ARG ALPINE_VERSION

FROM python:${PYTHON_VERSION}-alpine${ALPINE_VERSION}

RUN pip install pipenv
    
# RUN adduser -D -h /tmp/dummy dummy
# USER dummy
# WORKDIR /tmp/dummy

WORKDIR /tmp/app

COPY notejam notejam
COPY db.py db.py
COPY requirements.txt requirements.txt
COPY runserver.py runserver.py
COPY tests.py tests.py

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --deploy --system &&\
    python db.py

ENTRYPOINT ["python"]
CMD ["runserver.py"]