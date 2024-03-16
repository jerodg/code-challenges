FROM python:3.8

WORKDIR /app

COPY pyproject.toml ./
COPY poetry.lock ./

ENV POETRY_VERSION=1.0.5

RUN pip install "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY app.py ./app.py
COPY tests ./tests
COPY run.sh ./run.sh

EXPOSE 5000

CMD ["./run.sh"]
