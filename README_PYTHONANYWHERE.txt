PYTHONANYWHERE DEPLOY STEPS

1) Upload/push this project to GitHub.
2) PythonAnywhere Bash:
   git clone https://github.com/jansirani803durai-wq/charity-app.git
   cd charity-app
   python3.10 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py collectstatic --noinput

3) PythonAnywhere Web tab:
   Add a new web app -> Manual configuration -> Python 3.10

4) Virtualenv:
   /home/YOUR_USERNAME/charity-app/venv

5) WSGI file full content:
   import os
   import sys
   path = '/home/YOUR_USERNAME/charity-app'
   if path not in sys.path:
       sys.path.append(path)
   os.environ['DJANGO_SETTINGS_MODULE'] = 'hopehands.settings'
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()

6) Static files:
   URL: /static/
   Directory: /home/YOUR_USERNAME/charity-app/staticfiles

7) Reload web app.
