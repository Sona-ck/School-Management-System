from rest_framework import serializers
from scholarship.models import Scholarship

class android_serialiser(serializers.ModelSerializer):
    class Meta:
        model=Scholarship
        fields='__all__'