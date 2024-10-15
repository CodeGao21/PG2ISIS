from django.db import models
from django.contrib.auth.models import User

from broker.models import Broker
from property.models import Property

class Lead(models.Model):
    LEAD = 'Lead'
    PROSPECTO = 'Prospecto'
    CLIENT= 'Cliente'

    CHOICES_STATUS = (
        (LEAD, 'Lead'),
        (PROSPECTO, 'Prospecto'),
        (CLIENT, 'Cliente')
    )

    ABIERTO = 'Abierto'
    CERRADO = 'Cerrado'
    PERDIDO = 'Perdido'

    CHOICES_STATE = (
        (ABIERTO, 'Abierto'),
        (CERRADO, 'Cerrado'),
        (PERDIDO, 'Perdido')
    )

    BROKER = 'Broker'
    LETRERO = 'Letrero'
    COMPREOALQUILE = 'CompreoAlquile'
    CAMPAÑAINSTAGRAM = 'CampañaInstagram'
    Otro = 'Otro'
    

    CHOICES_FUENTE = (
        (BROKER, 'Broker'),
        (LETRERO, 'Letrero'),
        (COMPREOALQUILE, 'CompreoAlquile'),
        (CAMPAÑAINSTAGRAM, 'CampañaInstagram'),
        (Otro, 'Otro')
    )

    

    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15,blank=True, null=True)
    property_interested = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True, related_name='interested_leads')
    broker = models.ForeignKey(Broker, on_delete=models.SET_NULL, null=True, blank=True, related_name='leads')
    fuente = models.CharField(max_length=30, choices=CHOICES_FUENTE, blank=True, null=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=LEAD)
    state = models.CharField(max_length=10, choices=CHOICES_STATE, default=ABIERTO)
    date= models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

