class Customer:
    def __init__(self,id,name,ticket):
        self.id=id
        self.name=name
        self.ticket=ticket


class Ticket:
    def __init__(self,time,price,movie,seat):
        self.price=price
        self.time=time
        self.movie=movie
        self.seat=seat

class Seat:

    def __init__(self,seatnum,screen):
        self.seatnum=seatnum
        self.screen=screen

class Screen:

    def __init__(self,location,movie):
        self.location=location
        # self.seat=Seat
        self.movie=movie

class Movie:

    def __init__(self,name,language,price):
        self.name=name
        self.language=language
        self.price=price


vishl=Customer(12,"vishal",ticket=1)
stranger=Movie("stranger things","english",1000)
svreen1=Screen("BLR",stranger)
A12=Seat(12,svreen1)

ticket=Ticket("9.3-pm",100,stranger,A12)
print(vishl.name)
print(ticket.price)
print(ticket.movie.name)
print(ticket.movie.language)









