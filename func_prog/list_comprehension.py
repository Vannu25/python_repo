# list, set and dict - comprehensions

# list comprehension

my_list = [char for char in "Vanashree"]
print(my_list)

my_list1 = [num ** 2 for num in range(0, 100)]
print(my_list1)

my_list2 = [num ** 2 for num in range(0, 100) if num % 2 == 0]
print(my_list2)

# set comprehension

my_list = {char for char in "Vanashree"}
print(my_list)

my_list1 = {num ** 2 for num in range(0, 100)}
print(my_list1)

my_list2 = {num ** 2 for num in range(0, 100) if num % 2 == 0}
print(my_list2)

# dict comprehension

simple_dict = {
    "a": 1,
    "b": 2
}

my_dict = {k: v ** 2 for k, v in simple_dict.items()}
print(my_dict)
