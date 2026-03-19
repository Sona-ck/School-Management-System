from rest_framework import serializers
from timetable.models import Timetable

class android_serialiser(serializers.ModelSerializer):
    class Meta:
        model=Timetable
        fields='__all__'