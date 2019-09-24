import sys
"This function can be called from terminal using import fibo module and append the path " \
"import fibo " \
"sys.path.append(r'the path where you have saved the file')"


def fibo_1(n):
    first = 0
    second = 1
    while first <= n:
        print(first, end='')
        first, second = second, first+second
        print()


def fibo_2(n):
    result = []
    first = 0
    second = 1
    while first <= n:

        first, second = second, first + second

    return result

