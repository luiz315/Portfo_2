#!/bin/bash
pip install -r requirements.txt --break-system-packages
python seproject/manage.py collectstatic --noinput