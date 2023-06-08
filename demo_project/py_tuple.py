# python tuples - like immutable lists. cannot be modified like list elements.

my_tuple = (1, 2, 3, 3, 4, 5)  # cannot be changed
print(len(my_tuple))
print(my_tuple.count(3))
print(my_tuple.index(3))
print(5 in my_tuple)

x, y, z, *other = (1, 2, 3, 4, 5)
print(x)
print(y)

# tuple has two methods - count() and index()


