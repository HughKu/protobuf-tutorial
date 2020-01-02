from proto.simple import person_pb2

####################################
# - New message
####################################

# 1. Make a new instance of Person
person = person_pb2.Person()

# 2. Assign value to a scalar field
person.id = 7654321
person.name = "Hugh"
person.email = "hughku@gmail.com"


####################################
# - Repeated field
####################################

# 1-1. add a new repeated field (method 1)
phone = person.phones.add()
phone.number = "abc"

# 1-2. add a new repeated field (method 2)
phone = person_pb2.Person.PhoneNumber(number="xyz")
person.phones.extend([phone])

print(f"**** Processed message: \n{person}")


####################################
# - Read/Write from/to serialize message
####################################

# write and read message
with open("simple_message.bin", "wb") as fp:
  person_sent = person.SerializeToString()
  fp.write(person_sent)

with open("simple_message.bin", "rb") as fp:
  person_received = person_pb2.Person()
  person_received.ParseFromString(fp.read())
  print(f"**** De-serialized message: \n{person_received}")