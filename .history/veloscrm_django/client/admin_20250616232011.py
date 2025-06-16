from django.contrib import admin  # haal Django’s admin-module binnen
from .models import Client       # importeer je Client-model uit models.py

# Zorg dat het Client-model zichtbaar en beheersbaar is in de Django Admin
admin.site.register(Client)
