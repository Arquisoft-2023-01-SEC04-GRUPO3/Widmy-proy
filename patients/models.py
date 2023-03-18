from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    blood_type = models.CharField(max_length=3,default='N/A')
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)



    def __str__(self):
        return '{}'.format(self.name)

