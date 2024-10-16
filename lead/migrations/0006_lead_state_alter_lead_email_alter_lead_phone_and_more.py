# Generated by Django 5.0.2 on 2024-03-12 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0005_lead_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='state',
            field=models.CharField(choices=[('', ''), ('Abierto', 'Abierto'), ('Cerrado', 'Cerrado'), ('Perdido', 'Perdido')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='lead',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('', ''), ('Lead', 'Lead'), ('Prospecto', 'Prospecto'), ('Cliente', 'Cliente')], default='', max_length=10),
        ),
    ]
