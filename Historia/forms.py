from django import forms
from .models import Historia

class HistoriaForm(forms.ModelForm):
    class Meta:
        model = Historia
        fields = [
            'patient',
            'value',
            'unit',
            'place',
            #'dateTime',
        ]

        labels = {
            'patient' : 'Patient',
            'value' : 'Value',
            'unit' : 'Unit',
            'place' : 'Place',
            #'dateTime' : 'Date Time',
        }
