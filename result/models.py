from django.db import models
from student.models import Student

class Result(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    subject = models.CharField(max_length=100)
    marks = models.IntegerField(default=0)

    def __str__(self):
        return self.subject