## Requirements

- Python 3.10.7
- Django 4.2.1

## Quickstart

Fill up variables in env.temp file
python -m venv <name of Envireonment>  # Create Virtual Environment
<name of Envireonment>/Scripts/activate  # Activate Virtual Environment
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
