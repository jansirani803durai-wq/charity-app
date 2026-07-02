Render Deploy Settings:
Build Command:
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate

Start Command:
gunicorn hopehands.wsgi:application

Environment Variables:
SECRET_KEY = Generate in Render
DEBUG = False
ALLOWED_HOSTS = *
