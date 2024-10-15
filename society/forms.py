from django import forms

from .models import Society

class AddSocietyForm(forms.ModelForm):
    class Meta:
        model= Society
        fields=('name','ruc','description')

        