from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.Serializer):
    temp = serializers.IntegerField()
    pressure = serializers.FloatField()
    humidity = serializers.FloatField()
    #dateandtime = serializers.DateTimeField()
    def create(self, validated_data):
        return Data.objects.create(**validated_data)