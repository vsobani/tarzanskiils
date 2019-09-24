import os


def create_file(file_name):
    user_input = input("Enter the text you want to write to a file ")
    file=open(file_name, 'a')
    file.write(user_input)
    file.close()


def read_file(file_name):
    if os.path.exists(file_name):
        file=open(file_name,'r')
        print(file.readline())
        file.close()
    else:
        print("The file does not exist")


def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print("the file does not exist")


def update_file(file_name):
    user_input=input("update the existing file ")
    if os.path.exists(file_name):
        file = open(file_name, 'a')
    else:
        print("The file does not exist")


# file_handling = input("choose the file handling operation create read delete update ")

file_name = input("Enter the file name ")

#
# while True:
#     if file_handling == "create":
#         create_file(file_name)
#         break
#     elif file_handling == "read":
#         read_file(file_name)
#         break
#     elif file_handling == 'update':
#         update_file(file_name)
#         break
#     elif file_handling == 'delete':
#         delete_file(file_name)
#         break
#     else:
#         break
