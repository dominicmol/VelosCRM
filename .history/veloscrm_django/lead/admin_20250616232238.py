from django.contrib import admin  # nodig om modellen in de Admin-site te tonen
from .models import Lead           # importeer het Lead-model

# zorg dat je Lead-model zichtbaar en beheersbaar is in Django Admin
admin.site.register(Lead)
