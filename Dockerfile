FROM python:3.10.5

COPY . /app

WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction


EXPOSE 8080

CMD flask run --host=0.0.0.0 --port=8080