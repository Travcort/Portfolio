#!/bin/bash
# Creating a virtual environment
python3 -m venv virtual

# Activating the virtual environment
.\virtual\Scripts\activate

# Installing the requirements
python3 -m pip install -r requirements.txt

# Collecting the static files
python3 manage.py collectstatic --noinput