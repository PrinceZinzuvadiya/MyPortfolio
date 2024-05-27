from django import forms
from .models import contactmodel

class contact_form(forms.ModelForm):
    class Meta:
        model = contactmodel
        fields = '__all__'
