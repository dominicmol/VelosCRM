# importeer User-model en render-functie (hoewel render hier niet wordt gebruikt)
from django.contrib.auth.models import User
from django.shortcuts import render

# importeer DRF’s viewsets, filters, Response en decorator voor function-based views
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

# importeer je Team-model om toegangscontrole per team te regelen
from team.models import Team

# importeer je Lead-model en de bijbehorende serializer
from .models import Lead
from .serializers import LeadSerializer

# stel paginatie in voor leads: 2 items per pagina
class LeadPagination(PageNumberPagination):
    page_size = 2

# ViewSet voor al je Lead-CRUD-operaties, inclusief zoeken en pagineren
class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    pagination_class = LeadPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('company', 'contact_person')  # zoeken op bedrijfsnaam of contactpersoon
    
    # bij het aanmaken vul je automatisch team en maker in
    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team=team, created_by=self.request.user)
    
    # bij update: als er 'assigned_to' meegegeven wordt, wijs dan die gebruiker toe
    def perform_update(self, serializer):
        member_id = self.request.data.get('assigned_to')
        if member_id:
            user = User.objects.get(pk=member_id)
            serializer.save(assigned_to=user)
        else:
            serializer.save()

    # beperk altijd de queryset tot leads van het team van de ingelogde gebruiker
    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)

# functie-based view om een lead te verwijderen, met team-check
@api_view(['POST'])
def delete_lead(request, lead_id):
    team = Team.objects.filter(members__in=[request.user]).first()
    # filter op team en lead-id, verwijder direct
    team.leads.filter(pk=lead_id).delete()
    return Response({'message': 'The lead was deleted'})
