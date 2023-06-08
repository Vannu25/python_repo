# dir is used for printing all variables and function names of the "mymodule"

txt = " Hello World "
x = txt.strip()
print(x)

a = txt.replace("H", "J")
print(a)

fruits = ["apple", "banana", "cherry"]
print(len(fruits))

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))

car.clear()
print(car)

a = 50
b = 10

if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")

# while loop quest
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

    # kwargs


def my_function(**kid):
    print("His last name is " + kid["lname"])


# inheritance

class Person:
    def __init__(self, fname):
        self.firstname = fname

    def printname(self):
        print(self.firstname)


class Student(Person):
    pass


x = Student("Mike")
x.printname()
