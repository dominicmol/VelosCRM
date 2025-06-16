from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

# client.views importeert ClientViewSet en NoteViewSet,
# dus je hoeft NoteViewSet hier niet apart te importeren.
# 'NoteViewSet' in main_router is ook overbodig als deze al via client.urls gaat.
# from client.views import NoteViewSet 

# main_router is waarschijnlijk niet nodig als alle viewsets via hun eigen app's urls.py gaan
# main_router = DefaultRouter()
# main_router.register('notes', NoteViewSet, basename='notes')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # AANPASSING HIER: Verwijder 'clients/' uit de prefix
    path('api/v1/', include('client.urls')), # <-- Dit is de correcte manier
    
    # Als 'main_router' niet meer nodig is, verwijder dan deze regel ook
    # path('api/v1/', include(main_router.urls)), 
    
    path('api/v1/leads/', include('lead.urls')),
    path('api/v1/teams/', include('team.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),

    # Serve je Vue-app
    path('', TemplateView.as_view(template_name='index.html'), name='spa'),
]

