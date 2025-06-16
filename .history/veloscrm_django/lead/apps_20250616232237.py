from django.apps import AppConfig  # basisconfiguratie voor de Lead-app

class LeadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # gebruik BigAutoField voor nieuwe velden
    name = 'lead'  # de naam van deze app, zoals gebruikt in INSTALLED_APPS
