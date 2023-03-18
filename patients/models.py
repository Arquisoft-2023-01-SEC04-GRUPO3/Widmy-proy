from django.db import models

class Variable(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    blood_type = models.CharField(max_length=3)
    weight = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return '{}'.format(self.name)

