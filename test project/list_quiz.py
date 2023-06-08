from typing import List

listOne = ['a', 'b', 'c', 'd']
listTwo = ['e', 'f', 'g']

newList = listOne + listTwo
print(newList)

newList = listOne.extend(listTwo)
print(newList)

aList = ["PYnative", [4, 8, 12, 16]]
print(aList[0][1])
print(aList[1][3])

sampleList: list[int] = [10, 20, 30, 40, 50]
print(sampleList[-2])
print(sampleList[-4:-1])

aList = [10, 20, 30, 40, 50, 60, 70, 80]
print(aList[2:5])
print(aList[:4])
print(aList[3:])

print('==============================')

sampleList = [10, 20, 30, 40, 50]
sampleList.append(60)
print(sampleList)

sampleList.append(60)
print(sampleList)

print('==============================')
my_list = ["Hello", "Python"]
print("-".join(my_list))

print("===================================")
resList = [x + y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
print(resList)

aList = [5, 10, 15, 25]
print(aList[::-2])

list1 = ['xyz', 'zara', 'PYnative']
print(max(list1))

aList = [1, 2, 3, 4, 5, 6, 7]
pow2 = [2 * x for x in aList]
print(pow2)

print('==============================')
sampleList = [10, 20, 30, 40]
del sampleList[0:6]
print(sampleList)

print('==============================')
aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)

print('==============================')
l = [None] * 10
print(l)
print(len(l))

aList = ['a', 'b', 'c', 'd']

newList = aList.copy()
print(newList)
newList = list(aList)
print(newList)

print('==============================')
sampleList = [10, 20, 30, 40, 50]
sampleList.pop()
print(sampleList)

sampleList.pop(2)
print(sampleList)