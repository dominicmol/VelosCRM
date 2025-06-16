from django.apps import AppConfig  # basisconfiguratie voor de Team-app

class TeamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # standaard type voor automatisch gegenereerde velden
    name = 'team'  # naam van de app, gebruikt in INSTALLED_APPS
