def greet(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

greet('vijay',age = 24,place ='nellai',number = 908045)