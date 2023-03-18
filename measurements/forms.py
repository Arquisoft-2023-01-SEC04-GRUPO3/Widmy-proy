from django import forms
from .models import Measurement

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
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
