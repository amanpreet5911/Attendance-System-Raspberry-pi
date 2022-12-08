from django.urls import path , include
from .views import *
urlpatterns = [
    path('', Home, name='Home'),
    path('attendance/', AttendanceViewfunc, name='Attendance'),
    path('users/', Users, name='Users'),
    path('attendance/list-view', AttendanceView.as_view(), name='Attendance-list-view'),
    path('attendance/month-view', AttendanceMonthArchiveView.as_view(), name='Attendance-month-view'),
        # Example: /2012/08/
    path('attendance/month-view/<int:year>/<int:month>/',
         AttendanceMonthArchiveView.as_view(month_format='%m'),
         name="archive_month_numeric"),
    # Example: /2012/aug/
    path('<int:year>/<str:month>/',
         AttendanceMonthArchiveView.as_view(),
         name="archive_month"),
]