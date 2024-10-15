from django import forms

from .models import Broker

class AddBrokerForm(forms.ModelForm):
    class Meta:
        model= Broker
        fields=('name', 'email', 'description','agency', 'phone')

        