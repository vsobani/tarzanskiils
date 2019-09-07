from datetime import date

date_of_birth=str(input("enter the date of birth"))
present_date=str(input(""))
second_in_year=365*24*60*60
birth_year=date_of_birth[6:]
month=date_of_birth[3:4]
day=date_of_birth[:2]

present_year=present_date[6:]
present_month=present_date[3:4]
present_day=present_date[:2]

age=(present_year-birth_year)*365*24*60*60

print str((age))