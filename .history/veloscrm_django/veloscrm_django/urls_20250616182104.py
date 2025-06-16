from django.contrib import admin
from django.urls import path, include
# Let op: DefaultRouter en NoteViewSet zijn hier waarschijnlijk overbodig als ze via client.urls worden opgenomen
# from rest_framework.routers import DefaultRouter
# from client.views import NoteViewSet

from django.views.generic import TemplateView

# main_router is waarschijnlijk overbodig als NoteViewSet via client.urls gaat
# main_router = DefaultRouter()
# main_router.register('notes', NoteViewSet, basename='notes')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Fix voor Clients (hopelijk al uitgevoerd)
    path('api/v1/', include('client.urls')), 
    
    # FIX VOOR LEADS HIER: Verander deze regel
    path('api/v1/', include('lead.urls')), # <--- VERANDER DEZE REGEL!
    
    # Als main_router niet meer nodig is, verwijder dan deze regel ook
    # path('api/v1/', include(main_router.urls)), 
    
    path('api/v1/teams/', include('team.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),

    # Serveer je Vue-app
    path('', TemplateView.as_view(template_name='index.html'), name='spa'),
]

