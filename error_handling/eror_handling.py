# error handling

# finally block runs regardless of any issue


try:
    age = int(input("What's your age? "))
    print(age)
except:
    print("Enter a valid number")

try:
    num = int(input('enter a number? '))
    var = num / 0
except ZeroDivisionError:
    print('Please enter a number higher than 0')
except Exception as e:
    print(e)
