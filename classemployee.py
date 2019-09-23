class Employee:
    def __init__(self,id,first_name,last_name,qualification,salary,email,phone):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.qualification=qualification
        self.salary=salary
        self.email=email
        self.phone=phone

    def get_id():
        return self.id

    def get_fullname(self):
        return self.first_name + " " + self.last_name

    def get_email(self):
        return self.email

    def get_contact(self):

        return self.phone

class Developer(Employee):
    pass


developer_1=Developer(1,"vishal","sobani","B.E",122,"vishal.sobani@gmail.com",2090909090)
developer_2=Developer(2,"tarzan","skills","B.E",132,"tarzan@skills.com",290090909)
developer_3=Developer(3,"viss","ss","B.E",2121,"vsiah@avdi.com",8948498)
# print(developer_1.get_id())
# print(developer_1.get_fullname())
# print(developer_1.get_email())
# print(developer_1.get_contact())
# print(developer_2.get_id())
# print(developer_2.get_fullname())
# print(developer_2.get_email())
# print(developer_2.get_contact())
# print(developer_3.get_email())
print(developer_3.get_fullname())
emp_1=Employee(3,"markques","brownie","B.E",2121,"vsiah@avdi.com",8948498)
print(Employee.get_fullname(developer_1))
print(Developer.get_fullname(emp_1))
print(Employee.get_contact((developer_2)))
