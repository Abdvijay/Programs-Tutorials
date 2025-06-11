def factorial(x):
    sum = 1
    for i in range(1,x+1):
        sum = sum * i
    return sum

number = int(input("Enter the number : "))
result = factorial(number)
print("Factorial of ",number," is = ",result)