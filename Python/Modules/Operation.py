from Calc import *

def inputs():
    a = int(input("Enter the number 1 : "))
    b = int(input("Enter the number 2 : "))
    return a,b
print("'Operation'")
print("1.Addition\n2.Subtratction\n3.Multiplication\n4.Division\n5.Modulus\n6.Square")
op = int(input("Choose one operation : "))
if op == 1 :
    a,b = inputs()
    print(addition(a,b))
elif op == 2:
    a,b = inputs()
    print(subtraction(a,b))
elif op == 3:
    a,b = inputs()
    print(multiplication(a,b))
elif op == 4:
    a,b = inputs()
    print(division(a,b))
elif op == 5:
    a,b = inputs()
    print(modulus(a,b))
else:
    a = int(input("Enter the number : "))
    print(square(a))