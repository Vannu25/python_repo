# dunder methods, also called as magic methods

class Toy:
    def __init__(self, color, age):
        self.color = color  # attributes
        self.age = age


action_figure = Toy('Blue', 0)
print(action_figure.color)
print(action_figure.age)
print(action_figure.__str__())
print(str(action_figure))