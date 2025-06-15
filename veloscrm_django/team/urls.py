# veloscrm_django/team/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TeamViewSet, UserDetail, get_my_team, add_member

router = DefaultRouter()
# register met lege prefix voor list/detail van teams
router.register('', TeamViewSet, basename='team')

urlpatterns = [
    # 1) custom actie om je eigen team op te halen
    path('get_my_team/', get_my_team, name='team-get-my-team'),
    # 2) custom actie om een member toe te voegen
    path('add_member/', add_member, name='team-add-member'),
    # 3) custom actie om detail van één member te bekijken
    path('members/<int:pk>/', UserDetail.as_view(), name='team-user-detail'),
    # 4) pas nu pas de standaard list/detail/create/update/delete endpoints
    path('', include(router.urls)),
]
