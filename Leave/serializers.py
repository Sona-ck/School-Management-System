from rest_framework import serializers
from Leave.models import Leave

class android_serialiser(serializers.ModelSerializer):
    tname = serializers.CharField(source='teacher.name')
    pname=serializers.CharField(source='parent.name')
    class Meta:
        model=Leave
        fields=['tname','pname','lv_id','no_of_leave','reason','status']