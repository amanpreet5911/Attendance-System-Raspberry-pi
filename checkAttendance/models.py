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


# class UserProfile(models.Model):
#     user = models.OneToOneField(
#         User, on_delete=models.CASCADE, related_name='rfid')
#     rfid = models.CharField(max_length=20, null=True, blank=True, unique=True)

#     @staticmethod
#     def get_rfid(self):
#         return self.rfid

#     def __str__(self) -> str:
#         return f'{self.user}'


# class Profile(models.Model):
#     rfid_uid = models.PositiveSmallIntegerField()
#     name = models.CharField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)
