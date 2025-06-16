from django.urls import path, include          # import voor URL-definities en includen van andere urlpatronen
from rest_framework.routers import DefaultRouter  # router om ViewSets automatisch van routes te voorzien

from .views import (TeamViewSet, UserDetail,   # importeer je views: ViewSet én function- en class-based views
                    get_my_team, add_member, UserRegistrationView)

# stel de router in voor TeamViewSet (basis-URL /)
router = DefaultRouter()
router.register('', TeamViewSet, basename='team')  # alle standaard actions (list, retrieve, create, etc.)

urlpatterns = [
    # endpoint om nieuwe gebruikers te registreren
    path('signup/', UserRegistrationView.as_view(), name='user-signup'),

    # haal het team op waar de ingelogde gebruiker bij hoort
    path('get_my_team/', get_my_team, name='team-get-my-team'),

    # voeg een bestaand lid toe aan je team
    path('add_member/', add_member, name='team-add-member'),

    # bekijk of bewerk details van een specifiek teamlid (user ID in pk)
    path('members/<int:pk>/', UserDetail.as_view(), name='team-user-detail'),

    # include alle automatisch door de router aangemaakte routes (list, detail, create, update, destroy)
    path('', include(router.urls)),
]
