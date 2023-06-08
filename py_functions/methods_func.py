# Methods VS Functions - allows to take actions on data types

# Functions - list, input, print

# Methods = .count, .reverse, .sort
# methods needs to be owned by something pre object or data types and then ., eg 'hello'.capitalize()


# docstring - to give brief info about any random function.

def some_name(name):
    """
    :param name: The function tests the params for name
    :return: it returns /prints name
    """
    print(f"my name is {name}")


help(some_name)  # gives info printed on terminal
# dunder method
print(some_name.__doc__)
some_name('Vanashree')


# clean code

def is_even(num):
    return num % 2 == 0


print(is_even(50))
print(is_even(51))


# code to check if num is even or odd

def even_or_odd(num):
    if num % 2 == 0:
        print("num is even")
    else:
        print("num is odd")


even_or_odd(5)


# *args and **Kwargs - arguments and keyword arguments
# Rule : params, *args, default params, ** kwargs

def super_func(*args):  # n num of parameters acn be added with including *
    return sum(args)


print(super_func(1, 2, 3))

# Walrus operator

a = "vanashree"

if (n := (len(a))) > 10:
    print(f"the length of {n} is too long")
else:
    print(f"The length of {n} is shorter")


