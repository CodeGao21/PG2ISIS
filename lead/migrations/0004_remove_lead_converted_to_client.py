# Generated by Django 5.0.2 on 2024-03-07 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0003_alter_lead_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='converted_to_client',
        ),
    ]
