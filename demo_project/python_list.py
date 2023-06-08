cart = ['notebook', "tops", "Laptop", "vaseline", "grapes"]
print(cart[0])
print(cart[::-1])
print(cart[0:])
print(cart[:])

# matrix - 2d & 3d arrays useful in data processing and in Machine learning

# list are in the form of an array.
# sets are in the form of collection.

# list methods

basket = [1, 2, 3, 4, 5]
print(len(basket))

# adding - it modifies the list, doesn't create a copy of the list.
basket.append(100)
basket.insert(2, 99)
basket.extend([10, 15, 20])
print(basket)

# removing -

basket.pop(2)
basket.pop()
basket.remove(100)
basket.clear()
print(basket)

# sorting the list
new_basket = ['a', 'x', 'b', 'c', 'd', 'd', 'e']
new_basket.sort()
new_basket.reverse()
print(new_basket[::-1])  # list slicing
print(new_basket)

# list unpacking.

a, b, c, *other = [1, 2, 3, 4, 5]
print(a)
print(b)
print(c)
print(other)
