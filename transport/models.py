from django.db import models
from django.utils import timezone
from student.models import Student  # Link to student table

class Transport(models.Model):
    vehicle_number = models.CharField(max_length=50)
    driver_name = models.CharField(max_length=100)
    route = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.vehicle_number} - {self.route}"


class TransportFee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='transport_fees')
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, related_name='fees')
    month = models.DateField()  # Use first day of the month, e.g., 2026-03-01
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(
        max_length=10,
        choices=[('Paid', 'Paid'), ('Pending', 'Pending')],
        default='Pending'
    )
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Transport Fee"
        verbose_name_plural = "Transport Fees"
        ordering = ['-month']  # Latest month first

    def __str__(self):
        return f"{self.student.name} - {self.month.strftime('%B %Y')} - {self.status}"