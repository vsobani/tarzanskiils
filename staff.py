class Staff:
    def  __init__(self,name,department,qualification,age):
        self.name=name
        self.department=department
        self.qualification=qualification
        self.age=age

    def get_name(self):
        print(self.name,"is my name")

    def get_dept(self):
        print(self.department,"is my department")

    def get_qualification(self):
        print(self.qualification,"is my qualification")



class Teacher(Staff):
    pass

    def teach(self):
        print(f"{self.name} teaches {self.department}")


class Priciple(Staff):
    pass

    def expels(self):
        print(f"{self.name} expels")


    def speeh(self):
        print(f"{self.name} gave speech today")



teacher_1=Teacher("vishal","physics","Ph.D",40)
priciple_1=Priciple("rohan","chemistry","M.S",10)

Teacher.get_name(teacher_1)
Teacher.teach(teacher_1)
Priciple.expels(priciple_1)
Priciple.speeh(priciple_1)