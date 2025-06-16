# URL-configuratie voor Lead-API endpoints
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeadViewSet, delete_lead

# router maakt standaard-CRUD-urls voor LeadViewSet
router = DefaultRouter()
router.register('leads', LeadViewSet, basename='leads')

urlpatterns = [
    # custom endpoint om een lead te verwijderen via functie-based view
    path('leads/delete_lead/<int:lead_id>/', delete_lead, name='delete_lead'),
    # voeg alle automatisch gegenereerde router-urls toe (lijst, detail, create, update, delete)
    path('', include(router.urls)),
]
