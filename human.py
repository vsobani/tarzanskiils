class Human:
    def  __init__(self,name,age,phone,color):
        self.name=name
        self.age=age
        self.phone=phone
        self.color=color

    def get_name(self):
        print(self.name,"is my name")

    def get_age(self):
        print(self.age,"is my age")

    def  get_contact(self):
        print(self.phone,"is my contact number")



class Male(Human):
    pass

    def work(self):
        print(f"{self.name} works in office ")


class Female(Human):
    pass

    def work_female(self):
        print(f"{self.name} take care of the house")

male_1=Human("vishal",12,12345678,"White")
female_2=Human("kiara",21,12312,"white")
male_2=Male("sobani",12,12345678,"White")

Male.get_name(male_1)
Male.get_age(male_1)
Male.get_contact(male_2)
Male.work(male_1)

Female.get_name(female_2)
Female.get_age(female_2)
Female.get_contact(female_2)
Female.work_female(female_2)