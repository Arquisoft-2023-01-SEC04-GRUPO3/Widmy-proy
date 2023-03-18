from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
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