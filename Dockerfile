FROM python:3.10.5

COPY . /app

WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction


EXPOSE 8080

CMD gunicorn -w 4 -b 0.0.0.0:8080 "app:create_app()"