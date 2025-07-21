def greet(name, **data):
    print(name)
    for i in data.keys():
        print(f'{i} : {data[i]}')

greet('vijay',age = 24,place ='nellai',number = 908045)