# Everything in python is an object
# OOP - object Oriented Programming
# use camel case for defining a class eg - class BIgObject, class -> instantiate -> instance(object)

# class BigObject:   # Class - acts like a blueprint
#     pass
#
#
# obj1 = BigObject()   # instantiate - can be instantiated n number of times on basis of blueprint
# print(type(obj1))


class PlayerCharacter:
    # class object attribute
    membership = True

    # dunder method or also called as magic method  , It is the constructor method
    def __init__(self, name, age):
        self.name = name  # attributes , dynamic
        self.age = age

    def run(self):
        print("Run")
        return 'done'

    def shout(self):
        print(f"My name is {self.name}")

    @classmethod
    def add_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def add_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('cindy', 25)
player2 = PlayerCharacter('sunny', 26)
print(player1.name)
print(player2.age)
print(player1.run())
print(player1.shout())

# class and static methods


print(PlayerCharacter.add_things(2, 3))  # - have access to the class directly

# static
print(PlayerCharacter.add_things2(2, 2))  # - have access to the class directly but not to constructor method attributes

# super function - The super() function returns an object that represents the parent class
# object introspection -

print(dir(player1)) # all available options are seen.


