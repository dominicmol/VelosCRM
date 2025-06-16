from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, NoteViewSet, delete_client

router = DefaultRouter()
router.register('clients', ClientViewSet, basename='clients')
router.register('notes', NoteViewSet, basename='notes')

urlpatterns = [
    path('clients/delete_client/<int:client_id>/', delete_client, name='delete_client'),
    path('', include(router.urls)),
]