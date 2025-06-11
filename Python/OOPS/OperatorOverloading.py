class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        r1 = self.m1 + other.m1
        r2 = self.m1 + other.m2
        s3 = Student(r1,r2)
        return s3
    
    def __str__(self):
        return '{} {}'.format(self.m1 , self.m2)
    
    def __gt__(self,other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1 > r2:
            return True
        else:
            return False

s1 = Student(95,90)
s2 = Student(85,90)

s3 = s1 + s2
print(s3)

if s1 > s2 :
    print("S1 student is greater")
else:
    print("S2 Student is greater")