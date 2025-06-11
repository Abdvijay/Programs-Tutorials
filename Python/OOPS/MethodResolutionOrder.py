class A:
    def __init__(self):
        print("A constructor called...")

    def method1(self):
        print("Method 1 is printing")

    def method2(self):
        print("Method 2 is printing")

class B:
    def __init__(self):
        print("B Constructor called...")

    def method3(self):
        print("Method 3 is printing")

    def method4(self):
        print("Method 4 is printing")


class C(A,B):
    def __init__(self):
        super().__init__()
    
    def method5(self):
        print("Method 5 is printing")

c = C()

"""
A constructor called...

#It always takes left side order first that's why it is called only A class Contructor
"""