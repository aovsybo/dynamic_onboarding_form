# forms.py
from django import forms
from .models import Establishment


class EstablishmentForm(forms.ModelForm):
    class Meta:
        model = Establishment
        exclude = '__all__',
