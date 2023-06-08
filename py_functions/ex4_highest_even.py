def highest_even(args):
    list1 = []
    for item in args:
        if item % 2 == 0:
            list1.append(item)

    return max(list1)  # max function


print(highest_even([10, 2, 5, 8, 11]))


# name = "bhumi \n"
#
# if name is not None:
#     print(name * 100)



