from rest_framework import serializers
from transport.models import Transportation

class android_serialiser(serializers.ModelSerializer):
    class Meta:
        model=Transportation
        fields='__all__'