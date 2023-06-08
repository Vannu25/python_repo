# fruits = ['apple', 'orange', 'banana', 'kiwi']
# new_fruits = [fruit for fruit in fruits if 'a' in fruit]
# print(new_fruits)
#
#
# number_list = [x for x in range(10) if x % 2 == 0]
# print(number_list)
#
# Given two lists of different lengths, the task is to write a Python program to get their elements alternatively and repeat the list elements of the smaller list till the
# larger list elements get exhausted.
# Input : test_list1 = ['a', 'b', 'c'], test_list2 = [5, 7, 3, 0, 1, 8, 4]
# Output : ['a', 5, 'b', 7, 'c', 3, 'a', 0, 'b', 1, 'c', 8, 'a', 4]

test_list1 = ['a', 'b', 'c']
test_list2 = [5, 7, 3, 0, 1, 8, 4]

result_list = []

smaller_list_length = min(len(test_list1), len(test_list2))

# Loop through both lists simultaneously, adding elements alternately
for i in range(smaller_list_length):
    result_list.append(test_list1[i])
    result_list.append(test_list2[i])

# If there are any remaining elements in the longer list, repeat the elements of the smaller list
if len(test_list1) > len(test_list2):
    remaining_list = test_list1[len(test_list2):]
else:
    remaining_list = test_list2[len(test_list1):]

# Loop through the remaining elements, adding them alternately with the repeated elements of the smaller list
for i in range(len(remaining_list)):
    result_list.append(remaining_list[i])
    result_list.append(test_list1[i % len(test_list1)])

print(result_list)

