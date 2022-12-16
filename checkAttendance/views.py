from django.shortcuts import render, redirect
import calendar
from datetime import date
from accounts.models import User
from .forms import MonthlyAttendance
from django.core.paginator import Paginator
from django.db import connection
# from .models import Profile
# Create your views here.


def base(request):
    return redirect('Home')


def Home(request):
    return render(request, 'base.html')


def Users(request):
    users = User.objects.all()
    paginator = Paginator(users, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'users': users.order_by('date_joined'),
        'page_obj': page_obj,
    }
    return render(request, 'users.html', context)


def AttendanceViewfunc(request):
    search = False
    users = request.GET.get('Search_by_user')
    if users is not None:
        users = User.objects.filter(
            username__icontains=request.GET['Search_by_user'])
        search = True
    else:
        users = User.objects.all()
        # tusers = Profile.objects.raw('select * from users')
        # with connection.cursor() as cursor:
        #     cursor.execute("select * from users")
        #     users = cursor.fetchall()
        #     print(users)
        # list(row)
        # print(row)

    paginator = Paginator(users, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    month = request.GET.get('month', date.today().month)
    year = date.today().year
    form = MonthlyAttendance(request=request)
    num_days = calendar.monthrange(date.today().year, int(month))[1]
    days = [date(year, int(month), day) for day in range(1, num_days+1)]
    context = {
        # 'users': users.order_by('date_joined'),
        'page_obj': page_obj,
        'users_count': users.count(),
        'days_list': days,
        'month': calendar.month_name[int(month)],
        'form': form,
        'search': search,
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
