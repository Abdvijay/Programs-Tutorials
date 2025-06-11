a = 5
try:
    print("Opened...!")
    b = int(input("Enter the b value : "))
    print(a/b)
except ZeroDivisionError as e :
    print("You cannot divide a number by Zero : ",e)
except ValueError as e:
    print("Invalid Input : ",e)
finally:
    print("Closed...!")