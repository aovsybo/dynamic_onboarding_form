FROM python:3

ENV DJANGO_ENV=${DJANGO_ENV} \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_VERSION=1.3.2 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry'

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip3 install poetry

RUN poetry install --no-root

COPY ./src ./src

COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x entrypoint.sh \
  && mkdir -p /app/media /app/static \
  && chmod +x /app/media/ /app/static/

ENTRYPOINT ["/app/entrypoint.sh"]
