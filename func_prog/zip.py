# zip -The zip() function returns a zip object, which is an iterator of tuples
# where the first item in each passed iterator is paired together,
# and then the second item in each passed iterator are paired together etc.

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

print(list(zip(list1, list2)))

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = list(zip(a, b))
print(x)
y = tuple(zip(a, b))
print(y)
