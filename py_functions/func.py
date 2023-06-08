# DRY
# arguments VS parameters
def say_hello(name, emoji):
    print(f"hello {name} {emoji}")


# positional arguments
say_hello('Vanashree', ':)')

# keyword arguments
say_hello(emoji=':))', name='Vannu')

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


def christmas_tree():
    star = '*'
    empty = ' '
    for i in picture:
        for j in i:
            if j == 1:
                print(star, end='')
            elif j == 0:
                print(empty, end="")
        print("")


christmas_tree()


# christmas_tree()

# return - keyword in python

def add(num1, num2):
    sum = num1 + num2
    return sum


print(add(4, 5))
print(add(4, 10))


# PEP 8 - python enhancement proposal - style guide for python code


