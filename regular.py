import re

small_pass=re.compile(r"[a-z]+")
upper_pass=re.compile(r"[A-Z]+")
number_pass=re.compile(r"[0-9]+")
length_pass=re.compile(r"\w{8,}")
password = input("Enter string to test: ")

if small_pass.search(password) and upper_pass.search(password) and number_pass.search(password) and length_pass.search(password):
    print("Strong password",password)
else:
    print("weak password",password)
