# Generated by Django 5.0.2 on 2024-03-06 17:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0012_alter_process_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='end_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
