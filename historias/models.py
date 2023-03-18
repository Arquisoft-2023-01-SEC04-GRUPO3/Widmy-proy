from django.db import models
from patients.models import Patient

class Historia(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=None)
    doctor = models.CharField(max_length=50,default=None)
    place = models.CharField(max_length=50,default=None)
    dateTime = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=500,default=None)
    diagnosis = models.CharField(max_length=50,default=None)

    def __str__(self):
        return '%s %s' % (self.patient, self.diagnosis)