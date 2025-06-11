class A:
    def __init__(self):
        print("A constructor...")

    def method1(self):
        print("Method 1 is printing")

    def method2(self):
        print("Method 2 is printing")

    def show(self):
        self.method1()
        self.method2()

class B(A):
    def __init__(self):
        super().__init__()
        
    def method3(self):
        print("Method 3 is printing")

    def method4(self):
        print("Method 4 is printing")

    def show(self):
        super().show()
        self.method3()
        self.method4()

class C(B):
    def method5(self):
        print("Method 5 is printing")
    
    def show(self):
        super().show()
        self.method5()

c = C()
c.show()

"""

Method 1 is printing
Method 2 is printing
Method 3 is printing
Method 4 is printing
Method 5 is printing

"""