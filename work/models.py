from django.db import models
from teacher.models import Teacher


class Work(models.Model):
    work_id = models.AutoField(primary_key=True)   # ✅ KEEP THIS

    title = models.CharField(max_length=200)
    description = models.TextField()

    subject = models.CharField(max_length=100)

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )

    publish_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'work'
        ordering = ['-created_at']

    def __str__(self):
        return self.title