from rest_framework import serializers
from student.models import Student

class android_serialiser(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'