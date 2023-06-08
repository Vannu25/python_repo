# Abstraction - it means hiding of information and giving access to only the info that is necessary.

class PlayerChar:
    def __init__(self, name, age):
        self.__name = name  # private var
        self.age = age

    def run(self):
        print(f"run")

    def speaking(self):
        print(f"My name is {self.__name} and I am {self.age} years old")


player1 = PlayerChar('will buyers', 25)
print(player1.speaking())

# access modifiers - public, private, protected

_name = 'sunny'  # starting with underscore and a veriable , it means as a private var. Only works with classes
name = 'sunny'  # public var

# Data members of a class are declared protected by adding a single underscore ‘_’ symbol before the data member of
# that class.
# Data members of a class are declared private by adding a double underscore ‘__’ symbol before the data
# member of that class.
