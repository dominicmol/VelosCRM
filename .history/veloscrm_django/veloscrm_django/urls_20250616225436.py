from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Importeer de nieuwe UserRegistrationView
from .views import TeamViewSet, UserDetail, get_my_team, add_member, UserRegistrationView

router = DefaultRouter()
router.register('', TeamViewSet, basename='team')

urlpatterns = [
    # Nieuw: URL voor gebruikersregistratie
    path('signup/', UserRegistrationView.as_view(), name='user-signup'), 

    path('get_my_team/', get_my_team, name='team-get-my-team'),
    
    path('add_member/', add_member, name='team-add-member'),
    
    path('members/<int:pk>/', UserDetail.as_view(), name='team-user-detail'),
    
    path('', include(router.urls)),
]
