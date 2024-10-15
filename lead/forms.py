from django import forms

from .models import Lead

class AddLeadForm(forms.ModelForm):
    class Meta:
        model= Lead
        fields=('name', 'email', 'description', 'phone', 'property_interested', 'broker', 'fuente','status','state','date')

        
