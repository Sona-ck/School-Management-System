from django.db import models

class Parent(models.Model):

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    sid = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name