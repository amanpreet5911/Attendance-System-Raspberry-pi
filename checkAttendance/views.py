from django.shortcuts import render
import calendar
from datetime import date
from django_tables2 import SingleTableView
from .tables import AttendanceTable
from .models import Attendance
from django.views.generic.dates import MonthArchiveView
from django.contrib.auth.models import User
from .models import UserProfile
from django.db.models.query import Prefetch
from .forms import MonthlyAttendance

# Create your views here.


def Home(request):
    return render(request, 'base.html')


def attendance(request):
    return render(request, 'attendance.html')


class AttendanceView(SingleTableView):
    model = Attendance
    table_class = AttendanceTable
    template_name = 'attendance.html'


class AttendanceMonthArchiveView(MonthArchiveView):
    queryset = Attendance.objects.all()

    def get_queryset(self):
        return Attendance.objects.filter()
    date_field = "attendance"
    allow_future = True


def AttendanceViewfunc(request):
    month = request.GET.get('month', date.today().month)
    year = date.today().year
    form = MonthlyAttendance()
    users = User.objects.all()
    num_days = calendar.monthrange(date.today().year, int(month))[1]
    print(num_days)
    days = [date(year, int(month), day) for day in range(1, num_days+1)]
    context = {
        'users': users,
        'days_list': days,
        'month': calendar.month_name[int(month)],
        'form': form,
    }

    # We have users all month attendance list in the i.attndance
    # at = dict([(user,user.attendance.filter(attendance__month=month).all()) for user in users])
    # print(at)
    # nd = dict()
    # for day in days:
    #     for query in at.values():
    #         for q in query:
    #             if q.attendance.date() == day:
    #                 nd[q.user] = q.attendance.date()
    #                 # print(q.user,'->',q.attendance.date())
    # print(nd)
    # context['at'] = at
    # @register.filter(name='gma')
    # def get_monthly_attendance(user):
    #     print('herer')
    #     return user.attendance.filter(attendance__month=month).all()

    # @register.filter
    # def get_attendance(date,user):
    #     return Attendance.objects.filter(user=user,attendance__date=date)
    return render(request, 'attendancefunc.html', context)


def Users(request):
    users = User.objects.all()
    context = {
        'users': users,

    }

    return render(request, 'users.html', context)
