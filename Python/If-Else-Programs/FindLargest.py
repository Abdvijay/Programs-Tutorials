a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
c = int(input("Enter the 3rd number : "))

if ((a>b) and (a>c)):
    print("1st Number is the Largest")
elif ((b>a) and (b>c)):
    print("2nd Number is the Largest")
else:
    print("3rd Number is the Largest")