import os  # voor omgevingsvariabelen om Django-settings te bepalen
from django.core.wsgi import get_wsgi_application  # genereert de WSGI-applicatie voor je server

# stel in welke settings module geladen moet worden (veloscrm_django/settings.py)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'veloscrm_django.settings')

# maak de WSGI-toepassing; je webserver gebruikt deze om HTTP-verzoeken af te handelen
application = get_wsgi_application()
