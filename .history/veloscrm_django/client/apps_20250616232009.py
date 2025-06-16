from django.apps import AppConfig  # basisconfiguratie voor je Django-app

class ClientConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # standaard type voor automatisch gegenereerde velden
    name = 'client'  # naam van de app, gebruikt in INSTALLED_APPS

