# veloscrm_django/urls.py

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from django.views.generic import RedirectView

from client.views import NoteViewSet

# DRF-router voor notes
main_router = DefaultRouter()
main_router.register('notes', NoteViewSet, basename='notes')

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # API-endpoints
    path('api/v1/clients/', include('client.urls')),
    path('api/v1/', include(main_router.urls)),
    path('api/v1/leads/', include('lead.urls')),
    path('api/v1/teams/', include('team.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
]

# root => /static/index.html
urlpatterns += [
    path('', RedirectView.as_view(url='/static/index.html', permanent=False), name='spa'),
    # alle “deep” routes (history-mode) ook laten vallen op index.html
    re_path(r'^(?:.*)/?$', RedirectView.as_view(url='/static/index.html', permanent=False)),
]

