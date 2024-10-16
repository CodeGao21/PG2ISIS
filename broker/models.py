from django.db import models
from django.contrib.auth.models import User

class Broker(models.Model):

    name= models.CharField(max_length=255)
    email=models.EmailField()
    description=models.TextField(blank=True, null=True)
    agency= models.CharField(max_length=255, null=True, blank=True)
    phone=models.CharField(max_length=15)
    created_by = models.ForeignKey(User, related_name='brokers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

