# python sets - unordered collection of unique objects.
# set acts like collections which returns only unique items, no duplicate item is returned
#
# my_sets = {1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9}
# my_sets.add(15)
# my_sets.add(2)  # it adds to set but returns the unique value only.
# print(my_sets)

# converting list to sets.


my_list = [1, 2, 3, 4, 4, 5, 6]
my_set = set(my_list)
print(my_set)
print(len(my_set))
my_set1 = {5, 6, 7, 8, 8}

new = my_set.union(my_set1)
print(new)
