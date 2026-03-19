from rest_framework import serializers
from parent.models import Parent

class android_serialiser(serializers.ModelSerializer):
    class Meta:
        model=Parent
        fields='__all__'