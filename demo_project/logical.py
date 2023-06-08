# conditional logics.


if_old = True
if_licensed = True

if if_old and if_licensed:
    print("eligible to ride!")
else:
    print("not eligible to ride")

print("none")

# for the conditional logics - booleans are important.

# truthy and falsy  - values converted to bool are considered as true and null and empty values are considered as false


username = "van"
password = "1234"  # - if it is empty then this value is considered as false in boolean state

if username and password:
    print("the details are entered")

else:
    print("the details are not mentioned")

print("kook")

# ternary operator - shortcut for few conditions, also called as conditional expression

is_friend = False

can_message = "can message" if is_friend else "cannot message"  # ternary operator
print(can_message)

# short-circuiting - either of the condition needs to be true

is_hungry = True
is_foodie = False

# print(is_hungry or is_foodie)
if is_foodie or is_hungry:
    print("food is love :)")

# logical operators - and, or , not , < , > <=, >= , == , !=
# In ASCII, and therefore in Unicode, lowercase letters are greater than all uppercase letters.
print('a' > 'A')
print('A' > 'a')

print(ord('a'))
print(ord('A'))

if_magician = False
if_expert = False

if if_magician and if_expert:
    print("You are a master magician")
elif if_magician and not if_expert:  # or can also be used...
    print("At least you are there...")
elif not if_magician:
    print("you need magic powers")

# is- checks in one memory location to be same, where in == checks equality of values

print(True is True)
print(True == 1)

print([] is [])
print([] == [])
