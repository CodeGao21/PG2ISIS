# Generated by Django 4.2.11 on 2024-10-14 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0002_broker_agency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broker',
            name='agency',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
