from django.contrib.auth.models import User
from django.db import transaction # Belangrijk: importeer transaction

from rest_framework import serializers

from .models import Team, Plan

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email", # Voeg email toe als je die wilt kunnen zien
        )

# NIEUWE SERIALIZER VOOR GEBRUIKERSREGISTRATIE
class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}) # Maak wachtwoord write-only en verplicht

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'email': {'required': True}} # Maak email verplicht

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Een gebruiker met dit e-mailadres bestaat al.")
        return value

    def create(self, validated_data):
        with transaction.atomic():
            password = validated_data.pop('password')
            user = User.objects.create(**validated_data)
            user.set_password(password) # Hash het wachtwoord
            user.save()

            # Automatisch een team aanmaken voor de nieuwe gebruiker
            # Zorg ervoor dat de 'created_by' relatie in je Team model verwijst naar User
            # en dat dit veld niet automatisch door andere logica wordt ingevuld als je dit wilt.
            Team.objects.create(name=f'{user.username}\'s Team', created_by=user)

            return user

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

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)
    plan = PlanSerializer(read_only=True)

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