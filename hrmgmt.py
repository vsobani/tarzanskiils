class Company:
    def __init__(self, company_name, location, employee, staff):
        self.company_name = company_name
        self.location = location
        self.employee = employee
        self.staff = staff


class Employee:

    def __init__(self, employee_id, employee_name, phone):

        self.employee_id = employee_id
        self.employee_name = employee_name
        self.phone = phone


class Candidate():

    def __init__(self, candidate_name, candidate_id):

        self.candidate_name = candidate_name
        self.candidate_id = candidate_id

class Staff():

    def __init__(self, staff_name, staff_id, staff_profile):
        self.staff_name = staff_name
        self.staff_id = staff_id
        self.staff_profile = staff_profile


vishal = Candidate("vishal sobani", 10)
security = Staff("security", 111, "security_dept")
tarzan = Employee(12, "tarzan", 90909090)
tarzanskills = Company("tarzanskills", "BLR", tarzan, security)

