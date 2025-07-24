def Students(name="Lakshi",age=20):
    print("Name : ",name)
    print("Age : ",age)

Students("Vijay",24) #Positional Arguments

Students(age=22,name="Swathi") #Keyword Arguments

Students() #Default Arguments

def greet(*data):
    print(data)
    for i in data:
        print(i)
greet("Vijay", "Swathi", "Essai") #Variable Length Arguments

class Student:
    def sum(self,*data):
        total = 0
        for i in data:
            total += i
        print("Sum is : ", total)

s1 = Student()
s1.sum(14,56,78,90) #Variable Length Arguments in Class Method