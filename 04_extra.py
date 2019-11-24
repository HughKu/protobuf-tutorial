from proto.simple import any_pb2
from proto.simple import person_pb2

####################################
# - New message
####################################
extra = any_pb2.ExtraType()
person = person_pb2.Person()
person.name = "Hugh"
person.id = 1234567
person.email = "xxx@yyy.com"

extra.person.CopyFrom(person)
extra.data_any.Pack(person)

if extra.data_any.Is(person_pb2.Person.DESCRIPTOR):
   person_unpackes = person_pb2.Person()
   extra.data_any.Unpack(person_unpackes)
   print(person_unpackes)


####################################
# - Read/Write from/to serialize message
####################################

# write and read message
with open("simple_extra.bin", "wb") as fp:
   data_sent = extra.SerializePartialToString()
   fp.write(data_sent)

with open("simple_extra.bin", "rb") as fp:
   data_received = any_pb2.ExtraType()
   data_received.ParseFromString(fp.read())
   print(f"**** De-serialized message: \n{data_received}")
