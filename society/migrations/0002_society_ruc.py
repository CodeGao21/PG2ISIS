# Generated by Django 5.0.2 on 2024-03-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('society', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='society',
            name='ruc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
