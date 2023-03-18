from rest_framework import serializers
from . import models


class HistoriaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'patient', 'doctor', 'motive', 'description', 'diagnosis', 'dateTime')
        model = models.Historia