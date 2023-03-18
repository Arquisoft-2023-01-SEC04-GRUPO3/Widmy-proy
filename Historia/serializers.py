from rest_framework import serializers
from . import models


class HistoriaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'patient', 'value', 'unit', 'place', 'time',)
        model = models.Historia