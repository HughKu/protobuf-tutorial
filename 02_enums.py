from python.__generated__.enums import day_pb2

#
# Make a new instance of Admin
#
# 1. Make a new instance of Birthday
birthday = day_pb2.Birthday()

# 2. Assign value to a enum field
birthday.day = day_pb2.DayOfTheWeek.FRI
birthday.month = day_pb2.MonthOfTheYear.OCT

print(birthday.day == day_pb2.DayOfTheWeek.FRI)

print(f"**** Processed message: \n{birthday}")
#
# - Read/Write from/to serialize message
#
# write and read message
with open("enum_message.bin", "wb") as fp:
   birthday_sent = birthday.SerializePartialToString()
   fp.write(birthday_sent)

with open("enum_message.bin", "rb") as fp:
   birthday_received = day_pb2.Birthday()
   birthday_received.ParseFromString(fp.read())
   print(f"**** De-serialized message: \n{birthday}")