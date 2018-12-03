from django import forms
from .models import Grocery

class GroceryForm(forms.ModelForm):
    class Meta:
        model = Grocery
        fields = (  'item', 'cost')


