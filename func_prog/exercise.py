from functools import reduce

# 1 Capitalize all the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
new_list = []

for item in my_pets:  # looping
    new_list.append(item.upper())
print(new_list)


# 1 Capitalize all the pet names and print the list using map function
def capitalize(string):
    return string.upper()  # map func


print(list(map(capitalize, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
my_numbers.reverse()

print(my_numbers)

print(tuple(zip(my_strings, my_numbers)))
print(tuple(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def percent(score):
    if score > 50:
        return True


print(list(filter(percent, scores)))

# 4 Combine all the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
my_numbers = [5, 4, 3, 2, 1]
scores = [73, 20, 65, 19, 76, 100, 88]


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, (my_numbers + scores)))
