from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/', include('client.urls')), 
    
    path('api/v1/', include('lead.urls')), 
    
    path('api/v1/teams/', include('team.urls')),
    
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),

    path('', TemplateView.as_view(template_name='index.html'), name='spa'),
]

