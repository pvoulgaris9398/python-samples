FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml .

RUN pip install --upgrade pip

RUN pip install --root-user-action=ignore .[otel]

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]