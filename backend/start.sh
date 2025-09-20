#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Run migrations
# alembic upgrade head

# Start Gunicorn
gunicorn api.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT