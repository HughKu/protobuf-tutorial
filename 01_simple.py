from python.__generated__.user import admin_pb2
#
# Make a new instance of Admin
#
admin = admin_pb2.Admin()

#
# Assign value to a scalar field
#
admin.id = 122
admin.name = "Hugh"
admin.email = "hughku@gmail.com"

# method 1 - add a new repeated field
phone = admin.phones.add()
phone.number = "abc"
phone.type = admin_pb2.Admin.PhoneType.WORK

# method 2 - add a new repeated field
phone = admin_pb2.Admin.PhoneNumber(number="xyz", type=admin_pb2.Admin.PhoneType.HOME)
admin.phones.extend([phone])

# write and read message
with open("simple_message.bin", "wb") as fp:
    admin_sent = admin.SerializePartialToString()
    fp.write(admin_sent)

with open("simple_message.bin", "rb") as fp:
    admin_received = admin_pb2.Admin()
    admin_received.ParseFromString(fp.read())
    print(admin_received)