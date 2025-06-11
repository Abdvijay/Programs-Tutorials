def Fibanocci(x):
    a , b = 0, 1
    for i in range(x):
        print(a,end=" ")
        a , b = b, a+b

number = int(input("Enter the number : "))
Fibanocci(number)