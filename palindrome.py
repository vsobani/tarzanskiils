
def largest_list():

    largest = [21, 2, 3, 43, 4, 5]

    print("list is greater using max function", max(largest))
    print("list is greater using slicing ", largest[-1])


largest_list()


num = int(input("Enter number of elements in list: "))


def user_input():
    user_list = []
    for i in range(1, num + 1):
        element = int(input("Enter elements: "))
        user_list.append(element)
        # user_list.sort()
    print("Largest element is the list is ", max(user_list))
    print("largest element in the list using slicing is ", user_list[-1])


user_input()

def Reverse(lst):
    for ele in lst:
        reversed(lst)
    print(ele)



lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

