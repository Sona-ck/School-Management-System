from django.db import models

# Create your models here.
class Timetable(models.Model):
    tt_id = models.AutoField(primary_key=True)
    date = models.DateField()
    subject = models.CharField(max_length=100)
    time = models.TimeField()
    division = models.CharField(max_length=45)
    timetable = models.CharField(max_length=450)

    class Meta:
        managed = False
        db_table = 'timetable'