import math


def find_factorial_math_func():
    num = int(input("Enter number to find factorial: "))
    factorial = math.factorial(num)
    print("factorial of {0} is {1}".format(num, factorial))


if __name__ == '__main__':
    find_factorial_math_func()
