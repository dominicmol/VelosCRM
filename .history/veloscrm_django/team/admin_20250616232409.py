from django.contrib import admin  # nodig om modellen in de Admin-site te tonen
from .models import Team, TeamMember, Plan  # importeer je Team-gerelateerde modellen

# maak Team beheersbaar via Django Admin
admin.site.register(Team)
# maak TeamMember beheersbaar via Django Admin
admin.site.register(TeamMember)
# maak Plan-beheer mogelijk in Django Admin
admin.site.register(Plan)
