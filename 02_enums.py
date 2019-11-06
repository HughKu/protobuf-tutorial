from python.__generated__.enums import day_pb2
#
# Make a new instance of Admin
#
birthday = day_pb2.Birthday()

birthday.day = day_pb2.DaysOfTheWeek.FRI
birthday.month = day_pb2.MonthOfTheYear.JUN

print(birthday.day == day_pb2.DaysOfTheWeek.FRI)
print(birthday)