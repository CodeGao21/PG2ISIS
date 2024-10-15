from django import forms

from .models import Process

class AddProcessForm(forms.ModelForm):
    class Meta:
        model= Process
        fields=('name','prop','stage','OnProgress','start_date','end_date','description')

        