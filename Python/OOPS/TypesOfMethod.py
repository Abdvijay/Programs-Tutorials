class Student:
    College = 'Hindusthan'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    @classmethod
    def getCollege(cls):
        return cls.College
    
    @staticmethod
    def info():
        print("This is type of method example")

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

s1 = Student(50,40,60)
s2 = Student(10,20,30)

s1.info()
print(Student.getCollege())
print(s1.avg())

s2.info()
print(Student.getCollege())
print(s2.avg())