# decorators - prefix is given with @ sign and then a name, supercharges the function
# higher order function - HOC eg - map , reduce , filter
# functions are first class objects which means that functions in Python can be used or passed as arguments.
# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,
# without permanently modifying it.

from time import time


def my_decorator(func):
    def wrap_func():
        print("******")
        func()
        print("******")

    return wrap_func()


@my_decorator
def greet():
    print("Hello!")


# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()


print(shout('Hello'))

yell = shout

print(yell('Hello'))


# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)


greet(shout)
greet(whisper)


#  functions can return another function

def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10))


# why do we need Decorators?
def performance(fn):
    def wrapper_func(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2 - t1} seconds')
        return result
    return wrapper_func()


@performance
def long_func():
    for i in range(1000000):
        var = i * 5
        return var


long_func()
