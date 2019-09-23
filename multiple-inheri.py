# class Calculate_addition:
#
#     def addition(self,num1,num2):
#         return num1+num2
#
# class Calculation2:
#     def Multiplication(self,a,b):
#         return a*b
# class Derived(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b
# d = Derived()
# print(d.Summation(10,20))
# print(d.Multiplication(10,20))
# print(d.Divide(10,20))


class Teacher:
    def __init__(self,subject,name,age,gender, department):
        self.name = name
        self.age = age
        self.gender = gender
        self.subject = subject
        self.department = department

    def teach_sub(self):
        return self.subject


class Staff:
    def __init__(self,name,department):
        self.department=department
        self.name = name

    def get_staff_details(self):
        return self.name + ' ' + self.department

class Principle(Teacher, Staff):

    def __init__(self,name,department, subject, age, gender):
        self.name=name
        self.department=department
        Teacher.__init__(self, subject, name, age, gender, department)
        Staff.__init__(self, name, department)

shoaib_khan = Principle("Shoaib Khan", "admin", "Python", 33, "Male")

print(shoaib_khan.get_staff_details())






