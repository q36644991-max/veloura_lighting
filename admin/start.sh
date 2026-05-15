#!/bin/bash
export PYTHONPATH=$PYTHONPATH:.

# Start Auth service in the background
gunicorn -b 0.0.0.0:5001 admin.backend.auth_service.app:app &

# Start Management Service in the foreground on the Render port
gunicorn -b 0.0.0.0:$PORT admin.backend.management_service:app
