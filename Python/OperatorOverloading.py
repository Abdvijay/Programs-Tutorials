class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self, other):
        m1 = self.m1 +  self.m2 
        m2 = other.m1 + other.m2
        return m1,m2
    
    def __gt__(self, other):
        if (self.m1 + self.m2) > (other.m1 + other.m2):
            return True

s1 = Student(70,90)
s2 = Student(50,60)

print(s1 + s2)

if s1 > s2:
    print("s1 is greater than s2")
