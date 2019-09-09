# even=int(input("Enter an integer from 1 to 50 "))
# while even<=50:
#     if even%2==0:
#         print(f"The even numbers are",even)
#     even=even+1
#
#
#
# input_integer=int(input("Enter the integer "))
# i=0
# while i<input_integer:
#     a=i**2
#     i=i+1
#     print("square of integers are",a)

# i=0
# sum=0
# while i<9:
#     input_key =int( input("Enter the integers "))
#     sum=sum+input_key
#     i=i+1
#     average=sum/10
# print("the average of intergers are",average)
# i=0
# while i<4:
#     i = i + 1
#     print(i*"*")
# print(" ",end='')

line_count=int(input("Enter the line count "))
current_line=1

while current_line<line_count:
    if current_line%2!=0:
        print(current_line*"*")
    current_line=current_line+1
#print (current_line)
#current_line=current_line-1
while current_line>=1:
    if current_line%2!=0:
        print(current_line*"*")
    current_line=current_line-1


