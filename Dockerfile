FROM python:3.9-slim as base
WORKDIR /code
EXPOSE 8001

FROM base as deps
RUN apt-get update \
  && apt-get install gcc -y \
  && apt-get clean
WORKDIR /code
COPY pyproject.toml ./
COPY poetry.lock ./
RUN pip install "poetry<2"
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN poetry export -f requirements.txt --output requirements-dev.txt --without-hashes --only dev
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

FROM base as tests
WORKDIR /code
COPY . .
COPY --from=deps /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY --from=deps /code/requirements-dev.txt ./
RUN pip install --no-cache-dir --upgrade -r /code/requirements-dev.txt
RUN pytest -vvs

FROM base as dev
WORKDIR /code
COPY --from=deps /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY . .
CMD rq worker platform_default -c settings --with-scheduler

FROM base as production
WORKDIR /code
COPY --from=deps /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY . .
CMD rq worker platform_default -c settings --with-scheduler
