# n = int(input())
# for i in range(1, int(input())):
#     print(i * (10 ** i - 1) // 9)

# 1 multiply by 10 ** 1 - 1 // 9


# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print


if __name__ == '__main__':
    N = int(input())

    my_list = []
    my_list.insert(0, 5)
    my_list.insert(1, 10)
    my_list.insert(0, 6)
    print(my_list)
    my_list.remove(6)
    my_list.append(9)
    my_list.append(1)
    my_list.sort()
    print(my_list)
    my_list.pop()
    my_list.reverse()
    print(my_list)

