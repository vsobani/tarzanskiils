
def addition(num1, num2):
    sum = num1 + num2
    return sum


def subtract(num1, num2):
    diff = num1 - num2
    return diff


def multiply(num1, num2):
    mul = num1 * num2
    return mul


def divide(num1, num2):
    try:
        div = num1 / num2
        return div
    except Exception:

        print("Zero division not possible")

while True:
    num1 = int(input("Enter the value of first number "))
    num2 = int(input("Enter the value of second number "))

    choose_operation = input("what operation you want to perform like addition,subtract,multiply,division or exit ")
    if choose_operation == 'addition':
        print(f"Addition of {num1} and {num2} is ",addition(num1, num2))
    elif choose_operation == 'subtract':
        print(f"Subraction of {num1} and {num2} is ",subtract(num1, num2))
    elif choose_operation == 'multiply':
        print(f"Multiplication of {num1} and {num2} is ",multiply(num1, num2))
    elif choose_operation == 'division':
        print(f"Division of {num1} and {num2} is ",divide(num1, num2))
    elif choose_operation == 'exit':
        print("Program finished execution")
        break


try:
    with open('vishal.txt','r dat') as file:
        print(file.read())
except Exception:
    print('Could not open file.log')
