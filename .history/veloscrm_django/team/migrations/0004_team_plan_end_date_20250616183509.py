from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_auto_20210527_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='plan_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
