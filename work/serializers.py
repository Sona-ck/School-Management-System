from rest_framework import serializers
from work.models import Work


class android_serialiser(serializers.ModelSerializer):
    tname=serializers.CharField(source='teach.name')
    class Meta:
        model= Work
        fields='__all__'