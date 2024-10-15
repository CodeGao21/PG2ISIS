from django.db import models
from django.contrib.auth.models import User

class Society(models.Model):

    name= models.CharField(max_length=255)
    ruc=models.CharField(max_length=255,blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='propierties', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name