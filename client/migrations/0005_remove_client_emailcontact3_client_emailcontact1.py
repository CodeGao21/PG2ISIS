# Generated by Django 5.0.2 on 2024-03-05 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_alter_client_ruc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='emailcontact3',
        ),
        migrations.AddField(
            model_name='client',
            name='emailcontact1',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
