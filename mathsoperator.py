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
    div = num1 / num2
    return div


while True:
    num1 = int(input("Enter the value of first number "))
    num2 = int(input("Enter the value of second number "))

    choose_operation = input("what operation you want to perform like addition,subtract,multiply,division ")
    if choose_operation == 'addition':
        print(addition(num1, num2))
    elif choose_operation == 'subtract':
        print(subtract(num1, num2))
    elif choose_operation == 'multiply':
        print(multiply(num1, num2))
    elif choose_operation == 'division':
        print(divide(num1, num2))
    elif choose_operation == 'exit':
        print("Program finished execution")
        break



