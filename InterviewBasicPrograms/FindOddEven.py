def number_check():
    # Get user input
    num = input("Enter the number to check odd or even")

    if (int(num) % 2) == 0:
        print("{0} number is even".format(num))
    else:
        print("{0} number is odd".format(num))


if __name__ == '__main__':
    number_check()
