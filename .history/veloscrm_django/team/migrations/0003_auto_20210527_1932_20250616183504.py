from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20210514_0455'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='plan_status',
            field=models.CharField(choices=[('active', 'Active'), ('cancelled', 'Cancelled')], default='active', max_length=20),
        ),
        migrations.AddField(
            model_name='team',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='stripe_subscription_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
