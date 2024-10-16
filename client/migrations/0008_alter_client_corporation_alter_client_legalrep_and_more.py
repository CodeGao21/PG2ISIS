# Generated by Django 4.2.11 on 2024-10-14 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_alter_client_broker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='corporation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='legalrep',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='maincontact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='ruc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
