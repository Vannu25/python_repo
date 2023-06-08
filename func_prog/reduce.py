# reduce -t gives you a single value for a set of values by reducing a list to a single cumulative value. For example,
# if you have a list of scores, and you want to compute an average score,
# you can reduce that list using the reduce function in Python.
# reduce(fun,seq) function is used to apply a particular function passed in its
# argument to all the list elements mentioned in the sequence passed along.
# This function is defined in “functools” module.


from functools import reduce

my_list = [1, 2, 3, 4]


def accumulator(acc, item):
    print(acc, item)  # get func
    return acc + item


print(reduce(accumulator, my_list, 0))  # 6 + 4 = 10
print(reduce(accumulator, my_list, 10))
