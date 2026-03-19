from django.db import models
from student.models import Student
from parent.models import Parent


class Leave(models.Model):
    lv_id = models.AutoField(primary_key=True)

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)


    no_of_leave = models.IntegerField()

    date = models.DateField()

    reason = models.TextField()

    status = models.CharField(max_length=20, default='Pending')

    class Meta:
        db_table = 'leave'

