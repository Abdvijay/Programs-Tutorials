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