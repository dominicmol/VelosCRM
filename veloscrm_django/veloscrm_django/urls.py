# veloscrm_django/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

from client.views import NoteViewSet

# stel je DRF-router in
main_router = DefaultRouter()
main_router.register('notes', NoteViewSet, basename='notes')

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # je API endpoints
    path('api/v1/clients/', include('client.urls')),
    path('api/v1/', include(main_router.urls)),
    path('api/v1/leads/', include('lead.urls')),
    path('api/v1/teams/', include('team.urls')),

    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),

    # serve de Vue single-page app op de root
    path('', TemplateView.as_view(template_name='index.html'), name='spa'),
]
