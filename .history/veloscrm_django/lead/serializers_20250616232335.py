from rest_framework import serializers         # DRF’s serializer-framework
from .models import Lead                      # importeer het Lead-model
from team.serializers import UserSerializer    # voor geneste user-data bij 'assigned_to'

class LeadSerializer(serializers.ModelSerializer):
    # toon toegewezen gebruiker als geneste data, niet wijzigbaar via deze serializer
    assigned_to = UserSerializer(read_only=True)
    
    class Meta:
        model = Lead                           # koppel aan het Lead-model
        fields = (
            'id',
            'company',
            'contact_person',
            'email',
            'phone',
            'website',
            'confidence',
            'estimated_value',
            'status',
            'priority',
            'assigned_to',
            'created_at',
            'modified_at',
        )                                       # velden in de API-response
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at',
        )                                       # velden die niet via de API aangepast mogen worden
