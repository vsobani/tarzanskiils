age_input=int(input("Enter the age "))

if 2<=age_input<=5:
    print("got to kinddergaden")
elif 6<=age_input<=13:
    print("go to secondary school")
elif 14<=age_input<=16:
    print("go to high school")
else:
    print("got to college")


n=int(input("enter the integer "))

if n%2!=0:
    print("wierd")
elif 2>=n<=5:
    print("not wired")
elif 6>=n<=20:
    print("wierd")
elif (n%2==0 or n>20):
    print("not wired")

score=int(input("enter the score "))
if 25 < score <= 30:
    print("You have scored A grade")
elif 20 < score <= 25:
    print("You have scored B grade")
elif 15 < score <= 20:
    print("You have scored C grade")
elif 10 < score <= 15:
    print("You have scored D grade")
elif 5 < score <= 10:
    print("You have scored E grade")
elif 0 < score <= 5:
    print("You have scored F grade")
else:
    print("You have crossed the input")