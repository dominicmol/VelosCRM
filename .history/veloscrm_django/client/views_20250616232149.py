# imports voor authenticatie, REST-framework en HTTP-antwoorden
from django.contrib.auth.models import User
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.pagination import PageNumberPagination
from django.http import Http404

# importeer je eigen Team-, Client-, Note- en Lead-modellen en bijbehorende serializers
from team.models import Team
from .models import Client, Note
from lead.models import Lead
from .serializers import ClientSerializer, NoteSerializer

# pagina-instelling voor Client-lijsten (10 per pagina)
class ClientPagination(PageNumberPagination):
    page_size = 10

# ViewSet voor Client-CRUD en extra acties
class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    pagination_class = ClientPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'contact_person')

    # bij aanmaken vul je automatisch team en maker in
    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team=team, created_by=self.request.user)

    # filter lijst altijd op het team van de ingelogde gebruiker
    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)
    
    # extra endpoint: converteer een Lead naar een Client
    @action(detail=False, methods=['post'])
    def convert_lead_to_client(self, request):
        try:
            team = Team.objects.filter(members__in=[request.user]).first()
            lead_id = request.data.get('lead_id')
            if not lead_id:
                return Response({'detail': 'Lead ID is vereist om te converteren.'},
                                status=status.HTTP_400_BAD_REQUEST)

            lead = Lead.objects.filter(team=team).get(pk=lead_id)
            # maak nieuwe client aan op basis van lead-gegevens
            client = Client.objects.create(
                team=team,
                name=lead.company,
                contact_person=lead.contact_person,
                email=lead.email,
                phone=lead.phone,
                website=lead.website,
                created_by=request.user
            )
            lead.delete()  # verwijder de lead na conversie
            return Response(status=status.HTTP_200_OK)
        
        except Lead.DoesNotExist:
            return Response({'detail': 'Lead niet gevonden of behoort niet tot jouw team.'},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # log en rapporteer serverfouten bij conversie
            print(f"Fout bij het converteren van lead naar client: {e}")
            return Response({'detail': f"Serverfout bij conversie: {e}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ViewSet voor Note-CRUD, met beveiliging op team- en client-lidmaatschap
class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    
    # bij aanmaken controleer je team- en client-toegang
    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        if not team:
            return Response({'detail': 'Geen team gevonden.'},
                            status=status.HTTP_403_FORBIDDEN)

        client_id = self.request.data.get('client_id')
        try:
            client = Client.objects.get(pk=client_id, team=team)
        except Client.DoesNotExist:
            raise Http404("Client niet gevonden of niet van jouw team.")

        serializer.save(team=team, client=client, created_by=self.request.user)
    
    # filter notities op team, en optioneel op client_id
    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        if not team:
            return self.queryset.none()

        client_id = self.request.query_params.get('client_id')
        if client_id:
            return self.queryset.filter(client__pk=client_id, team=team)
        
        return self.queryset.filter(team=team)

# aparte functie om een client te verwijderen, met team-check
@api_view(['POST'])
def delete_client(request, client_id):
    team = Team.objects.filter(members__in=[request.user]).first()
    if not team:
        return Response({'detail': 'Geen team gevonden.'},
                        status=status.HTTP_403_FORBIDDEN)

    try:
        client = team.clients.get(pk=client_id)
        client.delete()
        return Response({'message': 'Client succesvol verwijderd.'},
                        status=status.HTTP_200_OK)
    except Client.DoesNotExist:
        return Response({'detail': 'Client niet gevonden of niet van jouw team.'},
                        status=status.HTTP_404_NOT_FOUND)
