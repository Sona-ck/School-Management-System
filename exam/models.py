from django.db import models
from teacher.models import Teacher

# Create your models here.


class Exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    exam_name = models.CharField(max_length=45)
    schedule = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()
    # teacher_id = models.IntegerField()
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject = models.CharField(max_length=45)

    class Meta:
        db_table = 'exam'
