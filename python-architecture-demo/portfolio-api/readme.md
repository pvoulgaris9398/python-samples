# Running

`cp .env.example .env`

`docker compose up --build`

- Open: `http://localhost:8000/health`
- Swagger: `http://localhost:8000/docs`

## Clean-Up

- Delete all build history in Docker Desktop:
  - `docker buildx history rm --all`

## Installing Dependencies

- Make sure `setuptools` is already installed in your `conda` environment
- Navigate to directory where `pyproject.toml` is and run:

`pip install -e .`

- Conda

## [structlog](https://www.structlog.org/en/stable/getting-started.html)