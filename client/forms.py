from django import forms

from .models import Client

class AddClientForm(forms.ModelForm):
    class Meta:
        model= Client
        fields=('commercialname', 'corporation', 'ruc', 'legalrep', 'maincontact', 'adresscontact', 'emailcontact','emailcontact1', 'emailcontact2', 'phonecontact',
                'description', 'broker')

    