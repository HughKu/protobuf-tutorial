from proto.simple import scalar_pb2

####################################
# - New message
####################################

data_holders = scalar_pb2.DataType()
# floating points
data_holders.data_float = -1023
data_holders.data_double = -1023
# integer (32 bits)
data_holders.data_int32 = -1023  # (variable-length encoding)
data_holders.data_uint32 = 1023  # (variable-length encoding)
data_holders.data_sint32 = -1023 # (variable-length encoding)
data_holders.data_fixed32 = 1023
data_holders.data_sfixed32 = 1023
# integer (64 bits)
data_holders.data_int64 = 1023   # (variable-length encoding)
data_holders.data_uint64 = 1023  # (variable-length encoding)
data_holders.data_sint64 = 1023  # (variable-length encoding)
data_holders.data_fixed64 = 1023
data_holders.data_sfixed64 = 1023
# string
data_holders.data_string = "-1023"
# boolean
data_holders.data_bool = True
# bytes
data_holders.data_bytes = b'1023'

print("**** Processed message: \n", data_holders)


####################################
# - Read/Write from/to serialize message
####################################

# write and read message
with open("enum_default.bin", "wb") as fp:
   data_holders_sent = data_holders.SerializePartialToString()
   fp.write(data_holders_sent)

with open("enum_default.bin", "rb") as fp:
   data_holders_received = scalar_pb2.DataType()
   data_holders_received.ParseFromString(fp.read())
   print(f"**** De-serialized message: \n{data_holders_received}")
