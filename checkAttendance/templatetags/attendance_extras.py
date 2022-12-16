from django import template
from accounts.models import Pi_attendance
from checkAttendance.models import Attendance
from datetime import date
register = template.Library()

year = date.today().year
month = date.today().month


@register.filter(name='gma')
def get_monthly_attendance(user):
    return user.attendance.filter(attendance__month=month).all()


@register.filter(name='gmd')
def get_attendance(user, date):
    a = Pi_attendance.objects.filter(employee=user, clock_in__date=date)
    # print(a)
    # a =  Attendance.objects.filter(user=user,attendance__date=date).values_list('attendance',flat=True)
    # query = Attendance.objects.filter(
    #     user=user, attendance__date=date).values_list('attendance', flat=True).query
    # print(query)
    if a:
        if a.count() > 1:
            l = ''
            for i in a:
                l += (i.clock_in.strftime('%m/%d/%Y, %H:%M:%S %p')) + '\n'
            return l
        else:
            l = list(a)[0]
            return l.clock_in.strftime('%m/%d/%Y, %H:%M:%S %p')

    return 'No Data Available'
