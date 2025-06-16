from django.contrib.auth.models import User  # ingebouwde User voor relaties en authenticatie  
from django.db import transaction             # voor het atomaire aanmaken van gebruiker + team

from rest_framework import serializers        # DRF’s serializer-framework

from .models import Team, Plan                # eigen Team- en Plan-modellen

# basis-serializer voor gebruikers, alleen uitlezen
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email", 
        )

# serializer voor het aanmaken van nieuwe gebruikers
class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}      # masker het wachtwoordveld in browserschermen
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'email': {'required': True}}  # e-mail verplicht bij registratie

    # controleer dat het e-mailadres nog niet in gebruik is
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Een gebruiker met dit e-mailadres bestaat al.")
        return value

    # bij aanmaak sla je in één transactie op: User + automatisch Team
    def create(self, validated_data):
        with transaction.atomic():
            password = validated_data.pop('password')
            user = User.objects.create(**validated_data)
            user.set_password(password)  # hash het wachtwoord
            user.save()

            # maak direct een nieuw team voor de gebruiker aan
            Team.objects.create(name=f"{user.username}'s Team", created_by=user)

            return user

# serializer voor Plan-modellen, alleen uitlezen
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = (
            "id",
            "name",
            "max_leads",
            "max_clients",
            "price"
        )

# serializer voor Team-modellen, met geneste serializers voor relaties
class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)  # toon teamleden als geneste User-data
    created_by = UserSerializer(read_only=True)           # wie het team heeft aangemaakt
    plan = PlanSerializer(read_only=True)                 # gekoppeld Plan, als geneste data

    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "members",
            "created_by",
            "plan",
            "plan_end_date"
        )
