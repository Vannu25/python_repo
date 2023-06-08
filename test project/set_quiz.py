sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.discard("Blue")
print(sampleSet)

print("=======================================================")

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 10, 30, 40, 80, 20, 50}

print(set1.issubset(set2))
print(set2.issuperset(set1))

print("=======================================================")

sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.discard("Orange")
# del sampleSet
print(sampleSet)

print("=======================================================")
# aSet = {1, 'PYnative', ['abc', 'xyz'], True}   - list and set can't be combined, need to uptype the set to list
# # print(aSet)

set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}

set3 = set2.difference(set1)
print(set3)

set1 = {10, 20, 30, 40}
set2 = {50, 20, "10", 60}

set3 = set1.union(set2)
print(set3)

sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.add("Blue")
sampleSet.add("Orange")
print(sampleSet)

aSet = {1, 'PYnative', ('abc', 'xyz'),
        True}  # - a tuple value. Note that tuples are immutable and can be elements of a set.
print(aSet)

set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}

set1.difference_update(set2)
print(set1)

sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.update(["Blue", "Green", "Red"])
print(sampleSet)

sampleSet = {"Yellow", "Orange", "Black"}
# print(sampleSet[1]) - syntax error, indexing is not supported in sets
