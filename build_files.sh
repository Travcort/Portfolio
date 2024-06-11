# Creating a virtual environment
python 3.9 -m venv virtual

# Activating the virtual environment
.\virtual\Scripts\activate

# Installing the requirements
pip3 install -r requirements.txt

# Collecting the static files
python3.9 manage.py collectstatic