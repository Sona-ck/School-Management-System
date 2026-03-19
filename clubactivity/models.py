from django.db import models

# Create your models here.
class Clubactivity(models.Model):
    clb_id = models.AutoField(primary_key=True)
    club = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)

    class Meta:
        db_table = 'clubactivity'
