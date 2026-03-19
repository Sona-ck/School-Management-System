from rest_framework import serializers
from notification.models import Notification

class android_serialiser(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields='__all__'