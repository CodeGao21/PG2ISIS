# Generated by Django 5.0.2 on 2024-03-04 17:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('property_interested', models.CharField(choices=[('Casa de Oro', 'Casa de Oro'), ('Santa Familia', 'Santa Familia'), ('La Legación', 'La Legación'), ('Callejón del Soná', 'Callejón del Soná'), ('Plazuela de Alfaro', 'Plazuela de Alfaro'), ('F&F Tower 39A', 'F&F Tower 39A'), ('F&F Tower 39B', 'F&F Tower 39B'), ('F&F Tower 39C - 39D', 'F&F Tower 39C - 39D'), ('Torre Generali 25B', 'Torre Generali 25B'), ('Torre Generali 8', 'Torre Generali 8'), ('Plaza Agora 17', 'Plaza Agora 17'), ('Plaza Agora 8', 'Plaza Agora 8'), ('Plaza Agora 9', 'Plaza Agora 9'), ('Plaza Agora 25A', 'Plaza Agora 25A'), ('Plaza Agora 25B', 'Plaza Agora 25B'), ('Plaza Agora 25C', 'Plaza Agora 25C')], default='Casa de Oro', max_length=50)),
                ('broker', models.CharField(max_length=255, null=True)),
                ('priority', models.CharField(choices=[('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta')], default='Media', max_length=10)),
                ('status', models.CharField(choices=[('Nuevo', 'Nuevo'), ('Contactado', 'Contactado'), ('Ganado', 'Ganado'), ('Perdido', 'Perdido')], default='Nuevo', max_length=10)),
                ('converted_to_client', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leads', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
