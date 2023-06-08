# inheritance - allow new object to take the properties of existing objets

class BaseClass:
    pass
    # {Body}


class DerivedClass(BaseClass):  # inherits the properties of the base class in to the derived class
    pass
    # {Body}


class Flower:
    def __init__(self, colour, name):
        self.colour = colour
        self.name = name

    def fragrance(self):
        print(f"Pleasant Fragrances of {self.name}")
        return True

    def bouquet(self):
        print(f"Bunch of {self.colour} color {self.name}")
        # return True


class event(Flower):

    def decor(self):
        print("flower decoration")


bunch = Flower('white', 'roses')
print(bunch.bouquet())
print(bunch.fragrance())

func = event('white', 'lilies')  # inherited from Flower
print(func.bouquet())
print(func.decor())

print(isinstance(bunch, Flower))  # true - as it is an instance of the class flower
print(isinstance(bunch, event))  # false - as the event class is not an instance of the bunch
