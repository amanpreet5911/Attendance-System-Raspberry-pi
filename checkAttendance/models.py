from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Attendance(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='attendance')
    attendance = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.user} {self.attendance.date()}'

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='rfid')
    rfid = models.CharField(max_length=20,null=True,blank=True)