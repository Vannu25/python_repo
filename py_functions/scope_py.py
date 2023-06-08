# scope - access to variables

a = 1


def parent():
    a = 10

    def confusion():
        # a = 5  # local scope
        return sum

    return confusion()


print(a)
print(parent())

# 1.Start with the local scope
# 2.Parent local
# 3.Global scope
# 4.build in python functions


# nonlocal keyword - parent local

# need of scope ?

x = 10
print(type(x))

x = "hello"[0]
print(x)

up = x.upper()
print(up)