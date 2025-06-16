# client/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, NoteViewSet, delete_client # Verwijder convert_lead_to_client uit deze import

router = DefaultRouter()
router.register('clients', ClientViewSet, basename='clients')
router.register('notes', NoteViewSet, basename='notes')

urlpatterns = [
    # VERWIJDER DEZE REGEL: path('convert_lead_to_client/', convert_lead_to_client, name='convert_lead_to_client'),
    path('clients/delete_client/<int:client_id>/', delete_client, name='delete_client'),
    path('', include(router.urls)),
]