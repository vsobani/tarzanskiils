class Employee:
    def __init__(self, first_name, last_name, employee_id, department, rate, hours_worked):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.department = department
        self.rate = rate
        self.hours_worked = hours_worked

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_salary(self, hours_worked):
        return self.rate * hours_worked


class Developer(Employee):

    def get_full_name(self):
        return super(Developer, self).get_full_name()
        # return self.first_name + ' ' + self.last_name

    def get_salary(self, hours_worked):
        self.incentive = 12
        return super(Developer, self).get_salary(hours_worked) + self.incentive

        # return self.rate * hours_worked



vishal = Employee ("vishal", "sobani", 12, "Developer", 1000, 12)
tarzan = Developer("tarzan", "skills", 1, None, 12, 121)
print(vishal.get_full_name())
print(vishal.department)
print(tarzan.get_full_name())
print(tarzan.department)
print(tarzan.get_salary(40))