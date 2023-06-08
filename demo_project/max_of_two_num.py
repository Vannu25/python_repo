def max_of_two_nums(a, b):
    if a >= b:
        return a
    else:
        return b


num1 = int(input("The 1st num is: "))
num2 = int(input("the 2nd num is: "))
print(max_of_two_nums(num1, num2))
