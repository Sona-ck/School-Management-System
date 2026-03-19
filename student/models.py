from django.db import models
from parent.models import Parent

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    class_field = models.CharField(db_column='class', max_length=100)
    division = models.CharField(max_length=1, choices=[('A','A'),('B','B'),('C','C'),('D','D')])

    gender = models.CharField(max_length=10, choices=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    ])

    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)

    father_occupation = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)

    dob = models.DateField()

    aadhar = models.CharField(max_length=12, unique=True)

    income = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)

    nativity = models.CharField(max_length=10, choices=(('urban','Urban'),('rural','Rural')))
    ncl_class = models.CharField(max_length=3, choices=(('yes','Yes'),('no','No')))

    caste = models.CharField(max_length=50)

    parent = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'student'