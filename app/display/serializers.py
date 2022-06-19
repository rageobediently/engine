from rest_framework import serializers
from .models import Metric


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = ('temp', 'pressure', 'humidity', 'dateandtime')
        extra_kwargs = {
            'dateandtime': {
                'read_only': True,
            },
        }
