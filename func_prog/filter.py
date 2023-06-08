# filter - If function is None, return the items that are true.
# The filter() function returns an iterator where the items are filtered through a function
# to test if the item is accepted or not.


my_list = [1, 2, 3, 4, 5]


def check_odd(item):
    if item % 2 != 0:
        return True


print(list(filter(check_odd, my_list)))
