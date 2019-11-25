import datetime

from proto.wkt import wkt_pb2


####################################
# - New message
####################################
extra = wkt_pb2.WktType()

dt = datetime.datetime(2019, 11, 24)
extra.data_timestamp.FromDatetime(dt)
print(f"FromDatetime: {extra.data_timestamp}")

extra.data_timestamp.FromJsonString("2019-11-25T00:00:01Z")
print(f"FromJsonString: {extra.data_timestamp.ToDatetime()}")

extra.data_timestamp.GetCurrentTime()
print(f"GetCurrentTime: {extra.data_timestamp.ToJsonString()}")

td = datetime.timedelta(1)
extra.data_duration.FromTimedelta(td)
print(f"FromTimedelta: {extra.data_duration.ToTimedelta()}")

extra.data_duration.FromMilliseconds(3500)
print(f"FromMilliseconds: {extra.data_duration.ToMilliseconds()}")

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
