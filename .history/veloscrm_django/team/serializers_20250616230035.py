from django.contrib.auth.models import User
from django.db import transaction

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
            "email", 
        )


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'email': {'required': True}} 

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Een gebruiker met dit e-mailadres bestaat al.")
        return value

    def create(self, validated_data):
        with transaction.atomic():
            password = validated_data.pop('password')
            user = User.objects.create(**validated_data)
            user.set_password(password) 
            user.save()

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