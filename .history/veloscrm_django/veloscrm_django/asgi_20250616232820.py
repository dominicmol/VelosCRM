import os  # nodig om omgevingsvariabelen in te stellen
from django.core.asgi import get_asgi_application  # importeert de ASGI-applicatiegenerator

# geef op welke settings-module Django moet gebruiken
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'veloscrm_django.settings')

# bouw de ASGI-toepassing op, die je server gebruikt om requests te verwerken
application = get_asgi_application()
