from rest_framework import serializers
from clubactivity.models import Clubactivity

class android_serialiser(serializers.ModelSerializer):
    class Meta:
        model=Clubactivity
        fields='__all__'