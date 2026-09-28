from django import forms
from .models import Laptop

class LaptopForm(forms.ModelForm):
    class Meta :
        model = Laptop
        fields= ['brand','price','imei','color']