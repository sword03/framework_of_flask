#!/usr/bin/env bash
export FLASK_COMMON_CONF=~/python/framework_of_flask/config/production.py
export FLASK_INSTANCE_CONF=~/python/framework_of_flask/instance/production.py
# python app.py

gunicorn -w 1 -b 127.0.0.1:6000 app:app --daemon