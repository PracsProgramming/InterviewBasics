def find_prime_number():
    num = int(input("Enter the number: "))

    if num > 1:

        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                print("{0} num is not prime".format(num))
                break
        else:
            print("{0} number is prime".format(num))
    else:
        print("number is not prime")


if __name__ == '__main__':
    find_prime_number()
