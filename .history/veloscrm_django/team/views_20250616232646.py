# importeer Django’s User-model en Http404 voor foutafhandeling
from django.contrib.auth.models import User
from django.http import Http404

# importeer DRF-componenten voor viewsets, generics en APIViews
from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# eigen modellen en serializers voor Team en User
from .models import Team
from .serializers import TeamSerializer, UserSerializer, UserCreateSerializer

# ViewSet voor alle CRUD-operaties op Team, alleen voor ingelogde gebruikers
class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    permission_classes = [IsAuthenticated]

    # beperk zichtbare teams tot die waar de gebruiker lid van is
    def get_queryset(self):
        return self.queryset.filter(members__in=[self.request.user])

    # bij aanmaken voeg je automatisch de maker ook als lid toe
    def perform_create(self, serializer):
        team = serializer.save(created_by=self.request.user)
        team.members.add(self.request.user)

# APIView voor ophalen en bijwerken van individuele gebruikers
class UserDetail(APIView):
    permission_classes = [IsAuthenticated]

    # helper om een User-objekt of 404 te krijgen
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    # GET → haal gebruikersgegevens op
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # PUT → update gebruikersgegevens
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(s
