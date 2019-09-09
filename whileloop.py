"""This is printing of even integers from 1 to 50 """

even=int(input("Enter an integer from 1 to 50 "))
while even<=50:
    if even%2==0:
        print(f"The even numbers are",even)
    even=even+1

"""This is printing square of a number"""

input_integer=int(input("Enter the integer "))
square=0
while square<input_integer:
    num=square**2
    square=square+1
    print(f"square of integers {num} are",num)


"""This is printing of pattern"""

i=0
sum=0
while i<9:
    input_key =int( input("Enter the integers "))
    sum=sum+input_key
    i=i+1
    average=sum/10
print("the average of intergers are",average)
i=0
while i<4:
    i = i + 1
    print(i*"*")
print(" ",end='')

line_count=int(input("Enter the line count "))
current_line=1

while current_line<line_count:
    if current_line%2!=0:
        print(current_line*"*")
    current_line=current_line+1

while current_line>=1:
    if current_line%2!=0:
        print(current_line*"*")
    current_line=current_line-1


