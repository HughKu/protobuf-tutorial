# import sys
# sys.path.append("/Users/linker/Documents/HughKu/protobuf-tutorial/__generated__")
# print(sys.path)

# from __generated__.simple import any_pb2
# from __generated__.simple import person_pb2

from proto.simple import any_pb2
from proto.simple import person_pb2

####################################
# - New message
####################################
data_any = any_pb2.ExtraType()
data_any.person.CopyFrom(person_pb2.Person())
#data_any.data_any.Pack({"Name": "Hugh"})



####################################
# - Read/Write from/to serialize message
####################################

# write and read message
with open("simple_extra.bin", "wb") as fp:
   data_sent = data_any.SerializePartialToString()
   fp.write(data_sent)

with open("simple_extra.bin", "rb") as fp:
   data_received = any_pb2.ExtraType()
   data_received.ParseFromString(fp.read())
   print(f"**** De-serialized message: \n{data_received}")
