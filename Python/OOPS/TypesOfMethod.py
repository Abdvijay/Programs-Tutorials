class Student:
    College = 'Hindusthan'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Class method
    # Class methods can access class variables and can be called on the class itself.
    @classmethod
    def getCollege(cls):
        return cls.College
    
    # Static method
    # Static methods do not access class or instance variables. They are utility functions that belong to the class.
    @staticmethod
    def info():
        print("This is type of method example")

    # Instance method
    # Instance methods can access instance variables and class variables.
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

s1 = Student(50,40,60)
s2 = Student(10,20,30)

s1.info()
print(s1.getCollege())
print(s1.avg())

s2.info()
print(s2.getCollege())
print(s2.avg())