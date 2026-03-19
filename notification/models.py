from django.db import models

class Notification(models.Model):

    notification = models.CharField(max_length=200)
    message = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    priority = models.CharField(
        max_length=20,
        choices=[
            ('Normal','Normal'),
            ('Important','Important'),
            ('Urgent','Urgent')
        ],
        default='Normal'
    )

    def __str__(self):
        return self.notification
