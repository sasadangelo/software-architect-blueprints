# -----------------------------------------------------------------------------
# Copyright (c) 2025 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy poetry files
COPY pyproject.toml poetry.lock* /app/

# Install Poetry
RUN pip install --no-cache-dir poetry

# Disable virtualenvs (use system python in container)
RUN poetry config virtualenvs.create false

# Install dependencies (production only)
RUN poetry install --only main --no-interaction --no-ansi

# Copy all source code (since Dockerfile is inside auth-service, '.' contiene tutto)
COPY . /app/

# Expose port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
