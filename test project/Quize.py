"""Variables and data types quiz """


def func1():
    x = 50
    return x


func1()
# print(x)  # name error , as x is defines in the local scope


aTuple = (1, 'Jhon', 1 + 3j)
print(type(aTuple[2:3]))

x = 75


def myfunc():
    # x = x + 1   # x i already assigned to 75 , outside the scope
    print(x)


myfunc()
# print(x)

print(type(0xFF))
print(type(range(5)))

print(bool(0), bool(3.14159), bool(-3), bool(1.0 + 1j))

x = 50


def fun1():
    x = 25
    print(x)


fun1()
print(x)

print(type({}) is set)

""" Operators and expression quiz"""

x = 10
y = 50
if x ** 2 > 100 and y < 100:
    print(x, y)
else:
    print('None')

x = 6
y = 2
print(x ** y)
print(x // y)

a = 4
b = 11
print(a | b)
print(a >> 2)

a = [10, 20]
b = a
b += [30, 40]
print(a)
print(b)

# syntax error code
# y = 10
# x = y += 2
# print(x)

x = 100
y = 50
print(x and y)

print(36 / 4)

print(2 % 6)  # checks for remainder

print(f"divisible{2 / 6}")

print(-18 // 4)  # round of to down / less value int

print(2 ** 3 ** 2)  # the expression goes from right to left i.e 3 ** 2 = 9, 2 ** 9 = 512

print('[%c]' % 65)

"""  Input and output quiz """
print('PYnative ', end='//')
print(' is for ', end='//')
print(' Python Lovers', end='//')

# print('%d %d %.2f' % (11, '22', 11.22)) - type error

# print(sep='--', 'Ben', 25, 'California') # syntax error

print('%x, %X' % (15, 15))

print('Ben', 25, 'California', sep='--')

print('%x, %X' % (15, 15))