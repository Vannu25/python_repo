for num in range(0, 10):
    print(num)

# enumerate - to get index for each item.

for i, char in enumerate("Helloo"):
    print(i, char)

for i, char in enumerate([1, 2, 3, 4, 5]):
    print(i, char)

for i, char in enumerate(list(range(100))):
    # print(i, char)
    if char == 50:
        print(f"The index of 50 is : {i}")

# reverse using range function

for _ in range(10, 1, -2):   # be default step count is 1
    print(_)


user = "Vanashree"
user_uppercase = user.upper()
for i in user_uppercase[::-1]:
    print(i)