from django.contrib.admin import site
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from client.views import delete_client
from lead.views import delete_lead

urlpatterns = [
    path('admin/', site.urls),
    
    path('api/v1/clients/delete_client/<int:client_id>/', delete_client, name='delete_client'),
    path('api/v1/leads/delete_lead/<int:lead_id>/', delete_lead, name='delete_lead'),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/v1/', include('client.urls')), 
    
    path('api/v1/', include('lead.urls')), 
    
    path('api/v1/teams/', include('team.urls')),
    
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),

    path('', TemplateView.as_view(template_name='index.html'), name='spa'),
]
