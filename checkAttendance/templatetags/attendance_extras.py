from django import template
from accounts.models import Pi_attendance
from datetime import date, datetime
import time
register = template.Library()

year = date.today().year
month = date.today().month
date_str = '10:00:00 AM'
late_time = datetime.strptime(date_str, '%H:%M:%S %p')


@register.filter(name='gla')
def get_late_attendance(user, date=None):
    if date:
        a = Pi_attendance.objects.filter(
            employee=user, clock_in__date=date, clock_in__time__gte=late_time).first()
        if a:
            return a.clock_in.strftime('%H:%M:%S %p')
        else:
            return None
    else:
        date = datetime.now().date()
        custom_date = datetime.strptime('18/12/2022', '%d/%m/%Y')
        a = Pi_attendance.objects.filter(
            employee=user, clock_in__date=date, clock_in__time__gte=late_time).first()
        print(a)
        if a:
            return a.clock_in.strftime('%H:%M:%S %p')
        else:
            return None


@register.filter(name='gmd')
def get_attendance(user, date):
    get_late_attendance(user)
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
                l += (i.clock_in.strftime('%H:%M:%S %p')) + '\n'
            return l
        else:
            l = list(a)[0]
            return l.clock_in.strftime('%H:%M:%S %p')

    return 'No Data Available'
