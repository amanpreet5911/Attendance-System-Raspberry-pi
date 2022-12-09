from django.shortcuts import render, redirect
import calendar
from datetime import date
from django.contrib.auth.models import User
from .forms import MonthlyAttendance

# Create your views here.


def base(request):
    return redirect('Home')

def Home(request):
    return render(request, 'base.html')


def Users(request):
    users = User.objects.all()
    context = {
        'users': users,

    }

    return render(request, 'users.html', context)


def AttendanceViewfunc(request):
    month = request.GET.get('month', date.today().month)
    year = date.today().year
    form = MonthlyAttendance(request=request)
    users = User.objects.all()
    num_days = calendar.monthrange(date.today().year, int(month))[1]
    days = [date(year, int(month), day) for day in range(1, num_days+1)]
    context = {
        'users': users,
        'users_count': users.count(),
        'days_list': days,
        'month': calendar.month_name[int(month)],
        'form': form,
    }
    return render(request, 'attendancefunc.html', context)


def UserMonthlyAttendance(request, pk=None):
    if not pk:
        return redirect('Attendance')
    month = request.GET.get('month', date.today().month)
    year = date.today().year
    form = MonthlyAttendance(request=request)
    user = User.objects.get(pk=pk)
    # attendance = user.attendance.filter(attendance__month=int(month)).all()
    num_days = calendar.monthrange(date.today().year, int(month))[1]
    days = [date(year, int(month), day) for day in range(1, num_days+1)]
    context = {
        'form': form,
        'user': user,
        # 'attendance': attendance,
        'days_list': days,
        'month': calendar.month_name[int(month)],
    }
    return render(request, 'UserAttendance.html', context)
