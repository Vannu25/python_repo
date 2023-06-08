# generators - it allow us to generate a sequence of value over time. A generator-function is defined like a normal
# function, but whenever it needs to generate a value, it does so with the yield keyword rather than return.
# Generators are useful when we want to produce a large sequence of values,
# but we don't want to store all of them in memory at once.
def generator_name(arg):
    # statements
    something = range(arg)
    yield something


# iterable - it allows any object that can be looped through.
# eg - range(100)

def make_list(num):
    result = []
    for i in range(num):
        # result.append(i * 2)
        result.append(i)
    return result


my_list = make_list(50)
print(my_list)


def generators_func(num):
    for i in range(num):
        yield i   # returns the recent data


# for ele in generators_func(100):
#     print(ele)

# g = generators_func(1)  # stop iteration
g = generators_func(10)
next(g)
next(g)
print(next(g))
print(next(g))  # StopIteration hwn called out of range
