from django import forms
from .models import Variable

class VariableForm(forms.ModelForm):
    class Meta:
        model = Variable
        fields = [
            'name',
            'age',
            'blood_type',
            'weight',
            'height'
        ]
        labels = {
            'name': 'Name',
            'age': 'Age',
            'blood_type': 'Blood Type',
            'weight': 'Weight',
            'height': 'Height'
        }