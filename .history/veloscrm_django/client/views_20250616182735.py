# client/views.py
from django.contrib.auth.models import User
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action # <-- Import 'action'
from rest_framework.pagination import PageNumberPagination
from django.http import Http404 # Zorg dat deze geïmporteerd is

from team.models import Team

from .models import Client, Note # Zorg dat Lead ook geïmporteerd is
from lead.models import Lead # <-- Zorg dat Lead model hier geïmporteerd is!
from .serializers import ClientSerializer, NoteSerializer # Zorg dat LeadSerializer ook hier is als je die nodig hebt

# ... (Je ClientPagination en ClientViewSet) ...

class ClientViewSet(viewsets.ModelViewSet):
    # ... (Bestaande code voor ClientViewSet) ...

    # Nieuwe actie voor conversie
    @action(detail=False, methods=['post']) # 'detail=False' betekent dat het niet op een specifiek client ID werkt
    def convert_lead_to_client(self, request):
        team = Team.objects.filter(members__in=[request.user]).first()
        lead_id = request.data.get('lead_id') # Gebruik .get() voor veiligheid

        if not lead_id:
            return Response({'detail': 'lead_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Zorg ervoor dat de lead aan het team van de gebruiker behoort
            lead = Lead.objects.filter(team=team).get(pk=lead_id)
        except Lead.DoesNotExist:
            raise Http404("Lead not found or does not belong to your team.")
        except Exception as e:
            # Voor debugging: log andere mogelijke errors
            print(f"Error fetching lead: {e}")
            return Response({'detail': f"Server error: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            client = Client.objects.create(
                team=team,
                name=lead.company,
                contact_person=lead.contact_person,
                email=lead.email,
                phone=lead.phone,
                website=lead.website,
                created_by=request.user
            )
            
            # OPTIONEEL: Verwijder de lead na conversie
            # lead.delete() 

            return Response(status=status.HTTP_200_OK) # Een lege 200 OK response
        except Exception as e:
            # Debugging voor client aanmaakfouten
            print(f"Error creating client from lead: {e}")
            return Response({'detail': f"Error converting lead: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ... (Je NoteViewSet en andere functies) ...

# VERWIJDER DE OUDE convert_lead_to_client functie HIERONDER als deze er nog staat!
# @api_view(['POST'])
# def convert_lead_to_client(request):
#    ...