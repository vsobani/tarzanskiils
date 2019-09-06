from decimal import Decimal
import fractions
print("i will count my chickens")
#i will count my chickens

print("hens",25+30/6)
# hens 30
print("roosters",100-25*3%4)

#roosters 1
print("now i will count my eggs")
# now i will count my eggs

print(3+2+1-5+4%2-2/4+6)
#6.5
print("is it true 3+2<5-7?")
#Error

print(3+2<5-7)
#False

print("what is 3+2?",3+2)
#5
print("what is 5-7 ?",5-7)
#-2

print("oh that's why its false.")

print("how abt some more")

print("is it greater?",5>-2)
#true
print("is it greater or equal?",5>=-2)
#True
print("is it less or equal?",5<=-2)
#false

print((25+3)*75.3)
#2108.4
print((35/3)*(25+4.9))
#348.634
print(Decimal(42.2+37.403)*(7%4+3-2*7))
#

r=5
pi=3.142
volume=4/3*pi*r*r*r
print(volume)

my_name="vishal"
last_name="sobani"
age=25
my_height=180
my_weigth=45
my_eyes="blue"
my_teeth="white"
contact=9090909090
weigth_in_kilo=my_weigth*0.453
my_address="Bangalore"
height_in_cm=my_height*2.54
print(f"hi im ",my_name)
print(f"im {age} years old")
print(f"he's is {my_height} inches tall")
print(f"im {height_in_cm} cm tall")
print(f"he's is {my_weigth} pounds heavy")
print(f"he's is {weigth_in_kilo} kg heavy")
print(f"he's got {my_teeth} teeth and {my_eyes} eyes %r, %t %")
print(f"he's is {my_height} inches tall")
total=my_weigth+my_height+age

print(f"if i add my age ,height and weight i get {total}")
