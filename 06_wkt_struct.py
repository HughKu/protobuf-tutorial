import datetime

from proto.wkt import wkt_pb2


####################################
# - New message
####################################
extra = wkt_pb2.WktType()

extra.data_struct["key_number"] = 1
extra.data_struct["key_bool"] = True
extra.data_struct["key_string"] = "Hello"
extra.data_struct["key_struct"] = { "Hello" : "World" }
extra.data_struct["key_list"] = [1, "2", 3, 4, 5]
extra.data_struct.get_or_create_struct("key4")["subkey"] = 11.0

print(extra.data_struct.get_or_create_list("key_list"))
print(extra.data_struct.get_or_create_struct("key_struct"))
print(extra.data_struct)

####################################
# - Read/Write from/to serialize message
####################################

# write and read message
# with open("wkt.bin", "wb") as fp:
#    data_sent = extra.SerializePartialToString()
#    fp.write(data_sent)

# with open("wkt.bin", "rb") as fp:
#    data_received = wkt_pb2.ExtraType()
#    data_received.ParseFromString(fp.read())
#    print(f"**** De-serialized message: \n{data_received}")
