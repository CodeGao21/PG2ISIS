# Generated by Django 5.0.2 on 2024-03-04 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_client_phonecontact'),
        ('property', '0002_alter_property_currentlease'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='currentlease',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='properties', to='client.client'),
        ),
    ]
