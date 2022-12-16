from datetime import datetime, timezone, date, timedelta
import calendar
# def daterange(start_date, end_date):
#     for n in range(int((end_date - start_date).days)):
#         yield start_date + timedelta(n)

# start_date = date(2022, 11, 1)
# end_date = date(2022, 12, 1)
# for single_date in daterange(start_date, end_date):
#     print(single_date.strftime("%Y-%m-%d"))

# year = date.today().year
# month = date.today().month
# num_days = calendar.monthrange(year, month)[1]
# days = [datetime.date(year, month, day) for day in range(1, num_days+1)]
# days_list = []
# for days in days:
#     days_str = days.strftime('%Y-%m-%d')
#     days_list.append(days_str)


# for i in range(1, 13):
#     print(i, calendar.month_name[i]), ',')


# Get the datetime object using datetime
# module
# dt_obj_w_tz = datetime.now()
# print(dt_obj_w_tz)

# # Add timezone information to the datetime
# # object
# dt_obj_w_tz = dt_obj_w_tz.replace(tzinfo=timezone.utc)
# print(dt_obj_w_tz)

# # Remove the timezone information from the datetime
# # object
# dt_obj_wo_tz = dt_obj_w_tz.replace(tzinfo=None)
# print(dt_obj_wo_tz)


print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
