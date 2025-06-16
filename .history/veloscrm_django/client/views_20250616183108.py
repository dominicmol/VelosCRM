from django.contrib.auth.models import User
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.pagination import PageNumberPagination
from django.http import Http404

from team.models import Team
from .models import Client, Note
from lead.models import Lead
from .serializers import ClientSerializer, NoteSerializer

class ClientPagination(PageNumberPagination):
    page_size = 10

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    pagination_class = ClientPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'contact_person')

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team=team, created_by=self.request.user)

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)
    
    @action(detail=False, methods=['post'])
    def convert_lead_to_client(self, request):
        try:
            team = Team.objects.filter(members__in=[request.user]).first()
            lead_id = request.data.get('lead_id')

            if not lead_id:
                return Response({'detail': 'Lead ID is vereist om te converteren.'}, status=status.HTTP_400_BAD_REQUEST)

            lead = Lead.objects.filter(team=team).get(pk=lead_id)

            if not team:
                return Response({'detail': 'Je bent niet gekoppeld aan een team of het team is niet gevonden.'}, status=status.HTTP_403_FORBIDDEN)

            client = Client.objects.create(
                team=team,
                name=lead.company,
                contact_person=lead.contact_person,
                email=lead.email,
                phone=lead.phone,
                website=lead.website,
                created_by=request.user
            )
            
            # lead.delete() 

            return Response(status=status.HTTP_200_OK)
        
        except Lead.DoesNotExist:
            return Response({'detail': 'Lead niet gevonden of behoort niet tot jouw team.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"Fout bij het converteren van lead naar client: {e}")
            return Response({'detail': f"Een serverfout is opgetreden bij de conversie: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    
    def perform_create(self, serializer):
        client_id = self.request.data.get('client_id')
        try:
            client = Client.objects.get(pk=client_id)
        except Client.DoesNotExist:
            raise Http404("Client not found.")
        serializer.save(client=client, created_by=self.request.user)
    
    def get_queryset(self):
        client_id = self.request.query_params.get('client_id')
        if client_id:
            return self.queryset.filter(client__pk=client_id)
        return self.queryset.none() # Of een andere standaard als client_id ontbreekt

@api_view(['POST'])
def delete_client(request, client_id):
    team = Team.objects.filter(members__in=[request.user]).first()
    client = team.clients.filter(pk=client_id)
    client.delete()
    return Response({'message': 'The client was deleted'})