from django.urls import path , include
from .views import *
urlpatterns = [
    path('Home/', Home, name='Home'),
    path('', base, name='base'),
    path('attendance/', AttendanceViewfunc, name='Attendance'),
    path('users/', Users, name='Users'),
    path('user-attendance/<int:pk>/',
         UserMonthlyAttendance, name='User-Attendance'),
]