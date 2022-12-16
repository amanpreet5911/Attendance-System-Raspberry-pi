from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Attendance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='attendance')
    attendance = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user} {self.attendance.date()}'
