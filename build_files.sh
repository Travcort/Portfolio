#!/bin/bash
# Creating a virtual environment
python -m venv virtual

# Activating the virtual environment
.\virtual\Scripts\activate

# Installing the requirements
python -m pip install -r requirements.txt

# Collecting the static files
python3.9 manage.py collectstatic