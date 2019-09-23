class Tarzanskills:

    def __init__(self,name,location,trainer,students):
        self.name=name
        self.location=location
        self.trainer=trainer
        self.students=students

class Trainer:

     def __init__(self,name,gender,qualification):
         self.name = name
         self.gender=gender
         self.qualification = qualification


class Students:

    def __init__(self,student_name,batch,laptop,books,subject):
        self.student_name=student_name
        self.batch=batch
        self.laptop=laptop
        self.books=books
        self.subject=subject

vishal = Students("vis",1,"dell","python training", "python")
varun = Trainer ("varun","male","software enginner")
tarzan = Tarzanskills("tarzan","Blr",varun,vishal)
print(varun.name)