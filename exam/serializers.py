from rest_framework import serializers
from exam.models import Exam

class android_serialiser(serializers.ModelSerializer):
    tname = serializers.CharField(source='teacher.name')
    class Meta:
        model=Exam
        fields=['tname','exam_id','exam_time','exam_date''schedule','exam_name','subject']