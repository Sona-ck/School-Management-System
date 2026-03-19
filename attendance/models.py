from django.db import models
from student.models import Student
from teacher.models import Teacher
from django.utils.timezone import now


class Attendance(models.Model):
    id = models.AutoField(primary_key=True)

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='attendance_records',
        null=True,
        blank=True
    )

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=[('Present', 'Present'), ('Absent', 'Absent')],
        default='Present'
    )

    date = models.DateField(default=now)

    def __str__(self):
        return f"{self.student.name} - {self.status} - {self.date}"