def find_armstrong_number():
    num = int(input("Enter the number to find armstrong number or not: "))
    numberofdigits=len(str(num))
    sum = 0
    arm_num = num

    while arm_num != 0:
        rem = arm_num%10
        sum = sum + (rem**numberofdigits)
        arm_num = arm_num //10

    if num == sum:
        print("{0} is an armstrong number".format(num))
    else:
        print("{0} is not an armstrong number".format(num))


if __name__ == '__main__':
    find_armstrong_number()


