from django.contrib.auth.models import User  # ingebouwde User voor relaties
from django.db import models  # basisveldtypes en model-ondersteuning
from team.models import Team  # Team-model om leads aan teams te koppelen

class Lead(models.Model):
    # mogelijke statussen voor een lead
    NEW = 'new'
    CONTACTED = 'contacted'
    INPROGRESS = 'inprogress'
    LOST = 'lost'
    WON = 'won'
    CHOICES_STATUS = (
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (INPROGRESS, 'In progress'),
        (LOST, 'Lost'),
        (WON, 'Won'),
    )

    # prioriteitsniveau’s voor opvolging
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    CHOICES_PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )

    # kerngegevens van de lead
    team = models.ForeignKey(Team, related_name='leads', on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    website = models.CharField(max_length=255, blank=True, null=True)

    # optionele schattingen en kansen
    confidence = models.IntegerField(blank=True, null=True)
    estimated_value = models.IntegerField(blank=True, null=True)

    # status en prioriteit, met standaards
    status = models.CharField(max_length=25, choices=CHOICES_STATUS, default=NEW)
    priority = models.CharField(max_length=25, choices=CHOICES_PRIORITY, default=MEDIUM)

    # toewijzing en audit-velden
    assigned_to = models.ForeignKey(
        User,
        related_name='assignedleads',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # wanneer de lead is aangemaakt
    modified_at = models.DateTimeField(auto_now=True)     # wanneer de lead voor het laatst is bewerkt
