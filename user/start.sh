#!/bin/bash
export PYTHONPATH=$PYTHONPATH:.

# Start microservices in the background
gunicorn -b 0.0.0.0:5001 admin.backend.auth_service.app:app &
gunicorn -b 0.0.0.0:5002 user.backend.product_service.app:app &
gunicorn -b 0.0.0.0:5003 user.backend.booking_service.app:app &
gunicorn -b 0.0.0.0:5004 user.backend.portfolio_service.app:app &
gunicorn -b 0.0.0.0:5005 user.backend.email_service.app:app &

# Start Gateway in the foreground on the Render port
gunicorn -b 0.0.0.0:$PORT user.backend.gateway.app:app
