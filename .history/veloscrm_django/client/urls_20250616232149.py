from django.urls import path, include           # nodig voor URL-configuratie
from rest_framework.routers import DefaultRouter  # router voor ViewSets
from .views import ClientViewSet, NoteViewSet, delete_client  # importeer je API-views

# stel een router in om automatisch standaard-CRUD-urls te maken
router = DefaultRouter()
router.register('clients', ClientViewSet, basename='clients')  # /clients/ → ClientViewSet
router.register('notes', NoteViewSet, basename='notes')        # /notes/   → NoteViewSet

urlpatterns = [
    # aparte route voor het verwijderen van een client via een function-based view
    path('clients/delete_client/<int:client_id>/', delete_client, name='delete_client'),
    # voeg alle automatisch gegenereerde router-urls toe
    path('', include(router.urls)),
]
