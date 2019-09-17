#
# def find_square():
#     num = 1
#     square=0
#     while num < 100:
#         for i in range(1,num):
#             if square==i**2:
#                 yield square
#             num += 1
#
#
# for element in find_square():
#     print(element)
#

def find_num_div7(num):
    start=1
    while start<=num:
        yield start
        start += 1

num=int(input("Enter the range of integers "))
for value in find_num_div7(num):
    if value % 7 == 0:
        print(value)

