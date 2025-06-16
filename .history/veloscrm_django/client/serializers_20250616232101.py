from rest_framework import serializers   # DRF’s serializer-framework
from .models import Client, Note        # importeer je Client- en Note-modellen

# bepaalt hoe Client-instanties naar JSON worden omgezet en terug
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client                   # koppel aan het Client-model
        fields = (
            'id',
            'name',
            'contact_person',
            'email',
            'phone',
            'website',
            'created_at',
            'modified_at',
        )                                # velden die in de API-response zitten
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at',
        )                                # velden die niet via de API aangepast mogen worden

# bepaalt hoe Note-instanties naar JSON worden omgezet en terug
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note                     # koppel aan het Note-model
        fields = (
            'id',
            'name',
            'body',
        )                                # velden die in de API-response zitten
