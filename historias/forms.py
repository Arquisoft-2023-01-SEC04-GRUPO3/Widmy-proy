from django import forms
from .models import Historia

class HistoriaForm(forms.ModelForm):
    class Meta:
        model = Historia
        fields = [
            'patient',
            'doctor',
            'description',
            'place',
            'diagnosis'
            #'dateTime',
        ]

        labels = {
            'patient' : 'Patient',
            'doctor' : 'Doctor',
            'place' : 'Place',
            'description' : 'Description',
            'diagnosis' : 'Diagnosis',
            #'dateTime' : 'Date Time',
        }
