from django.db import models
from django.contrib.auth.models import User

from broker.models import Broker

class Client(models.Model):

    commercialname= models.CharField(max_length=255)
    corporation= models.CharField(max_length=255, blank=True, null=True)
    ruc= models.CharField(max_length=255,blank=True, null=True)
    legalrep= models.CharField(max_length=255,blank=True, null=True)
    maincontact=models.CharField(max_length=255,blank=True, null=True)
    adresscontact= models.CharField(max_length=255, blank=True, null=True)
    emailcontact=models.EmailField(blank=True, null=True)
    emailcontact1=models.EmailField(blank=True,null=True)
    emailcontact2=models.EmailField(blank=True,null=True)
    phonecontact=models.CharField(max_length=40, blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.commercialname
