class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def config(self):
        print("Hi ",self.name)

std = Student('Vijay',24)
std2 = Student('Swathi',24)
std.config()
std2.config()