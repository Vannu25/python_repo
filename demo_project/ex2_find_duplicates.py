# clean
# readability.
# DRY
# predictability
# re-usable

dup_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for i in dup_list:
    # print(dup_list.count(i))
    if dup_list.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)
print(duplicates)

num = [1, 1, 2, 3, 4, 4, 5, 6, 5, 6]

new_num = []

for dupes in num:
    if num.count(dupes) > 1:
        if dupes not in new_num:
            new_num.append(dupes)
print(new_num)
