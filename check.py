import datetime
from datetime import date, timedelta
import calendar
# def daterange(start_date, end_date):
#     for n in range(int((end_date - start_date).days)):
#         yield start_date + timedelta(n)

# start_date = date(2022, 11, 1)
# end_date = date(2022, 12, 1)
# for single_date in daterange(start_date, end_date):
#     print(single_date.strftime("%Y-%m-%d"))

year = date.today().year
month = date.today().month
num_days = calendar.monthrange(year, month)[1]
days = [datetime.date(year, month, day) for day in range(1, num_days+1)]
days_list = []
for days in days:
    days_str = days.strftime('%Y-%m-%d')
    days_list.append(days_str)


for i in range(1, 13):
    print((i, calendar.month_name[i]), ',')
