#!/bin/bash
export PYTHONPATH=$PYTHONPATH:$(pwd):$(pwd)/seproject
pip install -r requirements.txt --break-system-packages
python seproject/manage.py collectstatic --noinput --clear
echo "--- static files ---"
ls -R staticfiles_build | head -n 100