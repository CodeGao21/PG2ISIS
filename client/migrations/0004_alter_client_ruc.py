# Generated by Django 5.0.2 on 2024-03-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_client_emailcontact2_client_emailcontact3_client_ruc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='ruc',
            field=models.CharField(max_length=255),
        ),
    ]
