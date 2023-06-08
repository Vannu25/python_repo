# MRO - Method Resolution  Order, the depth first search algorithm is used in MEO technique

class A:
    def method(self):
        print("A.method() called")


class B:
    pass


class C(B, A):
    pass


print(C.mro())

c = C()

c.method()
