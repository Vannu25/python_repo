# Python program to demonstrate
# multiple inheritance

# Base class1
class Mother:
    # mother_name = ""

    def mother(self, mother_name):
        self.mother_name = mother_name
        print(self.mother_name)


# Base class2


class Father:
    father_name = ""

    def father(self):
        print(self.father_name)


# Derived class


class Son(Mother, Father):
    def parents(self):
        print("Father :", self.father_name)
        print("Mother :", self.mother_name)


# Driver's code
s1 = Son()
s1.father_name = "RAM"
s1.mother_name = "SITA"
s1.parents()

