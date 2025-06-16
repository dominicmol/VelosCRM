# importeer de admin-site en URL-hulpmiddelen
from django.contrib.admin import site
from django.urls import path, include
from django.views.generic import TemplateView

# JWT-authenticatieviews voor token-uitgifte en vernieuwing
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# verwijzingen naar delete-functies uit je apps
from client.views import delete_client
from lead.views import delete_lead

urlpatterns = [
    # beheerinterface van Django
    path('admin/', site.urls),

    # custom endpoints om een client of lead te verwijderen
    path('api/v1/clients/delete_client/<int:client_id>/', delete_client, name='delete_client'),
    path('api/v1/leads/delete_lead/<int:lead_id>/', delete_lead, name='delete_lead'),

    # endpoints voor JSON Web Tokens (inloggen en token verversen)
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # include alle client-gerelateerde API-routes onder /api/v1/
    path('api/v1/', include('client.urls')),
    # include alle lead-gerelateerde API-routes onder /api/v1/
    path('api/v1/', include('lead.urls')),
    # include alle team-gerelateerde API-routes onder /api/v1/teams/
    path('api/v1/teams/', include('team.urls')),

    # endpoints voor gebruikersauthenticatie via Djoser
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),

    # serve de frontend (single-page app)
    path('', TemplateView.as_view(template_name='index.html'), name='spa'),
]
