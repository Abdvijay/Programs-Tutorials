class A:
    def show(self):
        print("Just A class show printing...")

class B(A):
    def show(self):
        print("Just B class show printing...")

obj = B()
obj.show()