# Generated by Django 5.0.2 on 2024-03-04 17:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('society', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('state', models.CharField(choices=[('Disponible', 'Disponible'), ('Ocupado', 'Ocupado')], default='Disponible', max_length=10)),
                ('condition', models.CharField(choices=[('Bueno', 'Bueno'), ('A Reparar', 'A Reparar')], default='Bueno', max_length=10)),
                ('parkings', models.IntegerField(default=0)),
                ('area1', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('address', models.CharField(default='N/A', max_length=255)),
                ('rentprice', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('mainteinprice', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('costxm2', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10)),
                ('maintxm2', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10)),
                ('maindescrp', models.TextField(blank=True, null=True)),
                ('pay', models.CharField(blank=True, choices=[('FCA', 'FCA'), ('Administracion', 'Administracion')], max_length=20, null=True)),
                ('leasestart', models.DateField(blank=True, null=True)),
                ('leasend', models.DateField(blank=True, null=True)),
                ('renov', models.CharField(blank=True, choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')], max_length=255, null=True)),
                ('notifyrenew', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to=settings.AUTH_USER_MODEL)),
                ('currentlease', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='properties', to='client.client')),
                ('society', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='society.society')),
            ],
        ),
    ]
