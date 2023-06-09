# under the hod of how generators work -

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            iterator * 5
            next(iterator)
        except StopIteration:
            break


"""
new eg for generator
"""


class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # this line allows us to use the current number as the starting point for the iteration
        MyGen.current = self.first   

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(1, 10)
for i in gen:
    print(i)
