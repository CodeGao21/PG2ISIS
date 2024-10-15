from django import forms
from .models import Property  

class AddPropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = (
            'name', 
            'description',
            'state',
            'condition',
            'society',
            'parkings', 
            'area1', 
            'address',
            'admin',
            'adminemail',
            'adminphone',
            'rentprice',
            'mainteinprice',
            'maindescrp',
            'pay',
            'poliza',
            'deposit',
            'lastincrease',
            'currentlease',
            'leasestart',
            'leasend',
            'increase',
            'renov',
            'notifyrenew',
        )
