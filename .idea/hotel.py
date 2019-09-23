class Hotel:
    def __init__(self,name,location,customers,Rooms):
        self.name=name
        self.location=location
        self.customers=Customers
       
    


class Rooms:
    def __init__(self,room_num,room_type,description,Customers):
        self.room_num=room_num
        self.room_type=room_type
        self.description=description
        


class Customers:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email


vishal=Customers("vis",90909090,"vis@hal.com")
room_222=Rooms("143","premium","2 bed room",vishal)
nova=Hotel("Nova","bangalore",vishal,room_222)

print(nova.name)
print(Hotel.__name__.__init__)