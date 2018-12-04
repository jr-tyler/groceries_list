from django import forms
from .models import Grocery, PiggyTopUp

class GroceryForm(forms.ModelForm):
    class Meta:
        model = Grocery
        fields = (  'item', 'cost')

class PiggyForm(forms.ModelForm):
    class Meta:
        model = PiggyTopUp
        fields = ('reason', 'amount')


