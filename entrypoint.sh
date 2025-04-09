#!/bin/bash
set -e

# Run migrations
if [ "$RUN_MIGRATIONS" = "true" ]; then
  echo "Running migrations..."
  alembic upgrade head
fi

# Start FastAPI
if [ "$APP_ENV" = "development" ]; then
  echo "Starting in development mode..."
  exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
else
  echo "Starting in production mode..."
  exec uvicorn app.main:app --host 0.0.0.0 --port 8000
fi