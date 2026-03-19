from rest_framework import serializers
from result.models import Result

class android_serialiser(serializers.ModelSerializer):
    sname=serializers.CharField(source='st.stdname')
    class Meta:
        model=Result
        fields=['sname','res_id','subject','result']