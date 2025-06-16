from django.contrib.auth.models import User  # ingebouwde User voor relaties
from django.db import models  # basisveldtypes en model-ondersteuning

# abonnementen of plans waar teams uit kunnen kiezen
class Plan(models.Model):
    name = models.CharField(max_length=255)            # naam van het plan
    max_leads = models.IntegerField(default=5)         # maximaal aantal leads toegestaan
    max_clients = models.IntegerField(default=5)       # maximaal aantal clients toegestaan
    price = models.IntegerField(default=0)            

    def __str__(self):
        return self.name  # toon plan-naam in admin en shell


class Team(models.Model):
    # mogelijke statussen voor het plan van dit team
    PLAN_ACTIVE = 'active'
    PLAN_CANCELLED = 'cancelled'
    CHOICES_PLAN_STATUS = (
        (PLAN_ACTIVE, 'Active'),
        (PLAN_CANCELLED, 'Cancelled'),
    )

    name = models.CharField(max_length=255)            # naam van het team
    members = models.ManyToManyField(
        User,
        through='TeamMember',
        related_name='teams'
    )                                                  # leden via tussenmodel TeamMember
    created_by = models.ForeignKey(
        User,
        related_name='created_teams',
        on_delete=models.CASCADE
    )                                                  # wie het team heeft aangemaakt
    created_at = models.DateTimeField(auto_now_add=True)  # aanmaakdatum
    plan = models.ForeignKey(
        Plan,
        related_name='teams',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )                                                 
    plan_status = models.CharField(
        max_length=20,
        choices=CHOICES_PLAN_STATUS,
        default=PLAN_ACTIVE
    )                                                 
    plan_end_date = models.DateTimeField(blank=True, null=True)  
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)     
    stripe_subscription_id = models.CharField(max_length=255, blank=True, null=True)  

    def __str__(self):
        return self.name  # toon team-naam in admin en shell

# tussenmodel om ManyToMany-relatie tussen User en Team expliciet te maken
class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)  # het team waar lid van is
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # de gebruiker die lid is

    class Meta:
        unique_together = ('team', 'user')  # zorg dat elke combinatie uniek is

    def __str__(self):
        return f"{self.user.username} - {self.team.name}"  # leesbare weergave van lidmaatschap
