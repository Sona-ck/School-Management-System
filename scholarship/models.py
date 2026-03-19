from django.db import models

class Scholarship(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    min_grade = models.IntegerField()
    max_grade = models.IntegerField()
    min_income = models.FloatField(null=True, blank=True)
    deadline = models.DateField()
    uploaded_by = models.ForeignKey(
        'teacher.Teacher',  # string reference avoids circular import
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title