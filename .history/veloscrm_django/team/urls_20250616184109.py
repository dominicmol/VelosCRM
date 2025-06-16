from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TeamViewSet, UserDetail, get_my_team, add_member

router = DefaultRouter()
router.register('', TeamViewSet, basename='team')

urlpatterns = [
 
    path('get_my_team/', get_my_team, name='team-get-my-team'),
   
    path('add_member/', add_member, name='team-add-member'),
    
    path('members/<int:pk>/', UserDetail.as_view(), name='team-user-detail'),
    
    path('', include(router.urls)),
]
