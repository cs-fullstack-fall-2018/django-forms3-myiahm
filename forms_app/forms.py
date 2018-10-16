from django import forms
from .models import NonProfit

class Forms(forms.ModelForm):
    class Meta:
        model = NonProfit
        fields = {'address','establishedDate','operatingBudget','name'}