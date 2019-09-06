"""

first_name= str(input("Enter your name :"))
last_name= str(input("Enter your last name : "))
salary=int(input("enter your salary :"))
age=int(input("enter your age :"))
print(f"my nasdme is {first_name} and my salary is {salary}")"""

student_name=str(input("enter the student name "))
student_age=int(input("enter the age of student "))
student_class=str(input("enter the class "))
physvisics_score=int(input("enter the score in physics "))
chemistry_score=int(input("enter the score in chemistry "))
biology_score=int(input("enter the score in biology "))
social=int(input("enter the score in social "))
english=int(input("score in english "))
hindi=int(input("score in hindi "))
total_marks=physics_score+biology_score+chemistry_score+english+hindi+social
average_scored=(total_marks/600)*100
print(f"{student_name} has scored {average_scored} % in exam")