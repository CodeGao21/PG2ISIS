# Generated by Django 5.0.2 on 2024-03-13 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_property_lastincrease_alter_property_costxm2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='newcontract',
            field=models.BooleanField(default=False),
        ),
    ]
