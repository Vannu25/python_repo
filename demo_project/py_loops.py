# test_list1 = ['a', 'b', 'c']
# test_list2 = [5, 7, 3, 0, 1, 8, 4]
#
# # Output : ['a', 5, 'b', 7, 'c', 3, 'a', 0, 'b', 1, 'c', 8, 'a', 4]
#
# for i in test_list1:
#     for x in test_list2:
#         print(i, x)

# iterable - it is an object or collection of items that can be iterated over
# iterable - list, dict, set, tuple, string - iterated - one by one to check each item.

users = {
    'name': 'Vanashree',
    'age': 25,
    'can_swim': False
}

for i in users.items():
    print(i)

for x in users.values():
    print(x)

for x in users.keys():
    print(x)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
add = sum(my_list)  # without forloop
# print(add)


i = 0
for x in my_list:
    i = i + x

print(i)
