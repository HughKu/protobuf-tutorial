from python.__generated__ import book_pb2
person = book_pb2.Person()

person.id = 122
person.name = "Hugh"
person.email = "hughku@gmail.com"

#
# - phone #1
#
phone_number = person.phones.add()
#hone_number = book_pb2.Person.PhoneNumber()
phone_number.number = "0972xxxxxx"
phone_number.type = book_pb2.Person.PhoneType.WORK

#
# - phone #2
#
phone_number = person.phones.add()
#hone_number = book_pb2.Person.PhoneNumber()
phone_number.number = "0988xxxxxx"
phone_number.type = book_pb2.Person.PhoneType.HOME

print(person.SerializeToString())