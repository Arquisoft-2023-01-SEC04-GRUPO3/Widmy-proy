from django import forms
from .models import Historia

class HistoriaForm(forms.ModelForm):
    class Meta:
        model = Historia
        fields = [
            'patient',
            'doctor',
            'motive',
            'description',
            'diagnosis'
            #'dateTime',
        ]

        labels = {
            'patient' : 'Patient',
            'doctor' : 'Doctor',
            'motive' : 'Motive',
            'description' : 'Description',
            'diagnosis' : 'Diagnosis',
            #'dateTime' : 'Date Time',
        }
