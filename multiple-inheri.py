class Calculate_addition:

    def addition(self, num1, num2):
        return num1+num2


class Calculate_Multiplication:
    def multiplication(self, num1, num2):
        return num1*num2


class Calulate(Calculate_addition,Calculate_Multiplication):

    def divide(self, num1, num2):
        return num1/num2


input_1 = Calulate()

print(input_1.addition(10,20))
print(input_1.multiplication(10,20))
print(input_1.divide(10,20))


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
varun_rathore = Principle("Varun Rathore", "Trainer", "Coding", 25, "Male" )
print(shoaib_khan.get_staff_details())
print(varun_rathore.get_staff_details())
print(varun_rathore.teach_sub())






