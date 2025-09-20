# Use official Python 3.11 slim image
FROM python:3.11-slim

# Environment variables to optimize Python behavior
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Working directory inside the container
WORKDIR /app

# Install system dependencies for PostgreSQL client and building packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app/

# Expose port for FastAPI app
EXPOSE 8000

# Entrypoint: Run migrations then start Uvicorn web server
CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000
