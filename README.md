# Analytics data processor

Python 3.9 worker for fetching, transforming, and storing analytics events.
The tests and local event-processing smoke test run without another repository
or cloud credentials.

## Tests with Docker

Run commands from this directory, which contains `pyproject.toml`.

```sh
docker build --platform linux/amd64 --target tests -t analytics-processor-tests .
```

The build installs the locked dependencies and runs the suite. Expected result:
35 passed. A failed test makes the build fail.

## Independent local processing test

This test uses disposable Redis and ClickHouse services on an internal Docker
network. It publishes no host ports. It sends two synthetic events through a real
RQ worker, the existing event processor, and the existing ClickHouse saver.

1. Start the services and run the test:

   ```sh
   docker compose run --build --rm smoke
   ```

2. Confirm this final output:

   ```text
   PASS: Redis enqueue -> RQ worker -> event processor -> ClickHouse; 2 exact rows
   ```

3. Remove this project's test containers, network, and test data:

   ```sh
   docker compose down --volumes --remove-orphans
   ```

If the test fails, still run step 3. The test does not exercise live provider
downloads, cloud storage, OAuth, screenshots, or the companion backend.

## Tests without Docker

Use Python 3.9 on Linux x86_64 and Poetry 1.x. Keep Poetry outside the project
virtual environment because the project locks older dependency versions.

```sh
poetry env use python3.9
poetry install --no-root
poetry run pytest -q
```

`--no-root` is required: this repository runs from its source directory.

Tests use mocks and synthetic identities, credentials, and event records.
Do not send fixture values to external services.

## Full worker operation

Runtime requires Redis, ClickHouse, and the analytics backend. Configure
`REDIS_HOST`, `REDIS_PASSWORD`, `BACKEND_BASE_URL`, `BACKEND_API_KEY_NAME`,
and `BACKEND_API_KEY_SECRET` locally. Use `platform-api-key` as the header
name when connecting to the accompanying backend.

Run `rq worker platform_default -c settings --with-scheduler`.
Provider integrations require separate local configuration.

## Source and fixture hygiene

Test identities, credentials, and event records are synthetic. `.gitignore`
excludes virtual environments, caches, build output, dependencies, and local
environment files. Keep those files out of source archives. Third-party
dependencies retain their original attribution.

This project is licensed under the MIT License. See [LICENSE](LICENSE).
