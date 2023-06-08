# encapsulation - binding of the data and functions that manipulate that data.

# when you create a class, it means you are implementing encapsulation

class Students:
    def __init__(self, name, rank, points):
        self.name = name
        self.rank = rank
        self.points = points

    # custom function
    def demofunc(self):
        print("I am " + self.name)
        print("I got Rank ", +self.rank)


# create 4 objects
st1 = Students("Steve", 1, 100)
st2 = Students("Chris", 2, 90)

st1.demofunc()
st2.demofunc()
