def add_or_multiply(num1, num2):
    prod = num1 * num2
    if prod <= 1000:
        return prod
    else:
        sum = num1 + num2
        return sum


print(add_or_multiply(20, 30))
print(add_or_multiply(40, 30))

var = "James" * 2 * 3
print(var)

salary = 8000


def printSalary():
    salary = 12000
    print("Salary:", salary)


printSalary()
print("Salary:", salary)

for i in range(1, 5):
    print(i)
else:
    print("this is else block statement")

x = 36 / 4 * (3 + 2) * 4 + 2  # bodmas
print(x)


def calculate(num1, num2=4):
    res = num1 * num2
    print(res)


calculate(5, 6)

listOne = [20, 40, 60, 80]
listTwo = [20, 40, 60, 80]

print(listOne == listTwo)
print(listOne is listTwo)

# sampleList = ["Jon", "Kelly", "Jessa"]
# sampleList.append(2, "Scott")
# print(sampleList)

var = "James Bond"
print(var[2::-1])

sampleSet = {"Jodi", "Eric", "Garry"}
sampleSet.add("Vicki")
print(sampleSet)

