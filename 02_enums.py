from python.__generated__.enums import day_pb2
#
# Make a new instance of Admin
#
birthday = day_pb2.Birthday()

birthday.day = day_pb2.DayOfTheWeek.FRI
birthday.month = day_pb2.MonthOfTheYear.JUN

print(birthday.day == day_pb2.DayOfTheWeek.FRI)
print(birthday)

# write and read message
with open("enum_message.bin", "wb") as fp:
    birthday_sent = birthday.SerializePartialToString()
    fp.write(birthday_sent)

with open("enum_message.bin", "rb") as fp:
    birthday_received = day_pb2.Birthday()
    birthday_received.ParseFromString(fp.read())
    print(birthday_received)