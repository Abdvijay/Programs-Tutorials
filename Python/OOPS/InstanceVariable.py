class Cars:
    wheels = 4
    def __init__(self,milage,name):
        self.milage = milage
        self.name = name

c1 = Cars(10,'BMW')
c2 = Cars(20,"TOYOTA")

Cars.wheels = 5
print(c1.name,c1.milage,c1.wheels)
print(c2.name,c2.milage,c1.wheels)