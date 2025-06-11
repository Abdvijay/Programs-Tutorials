year = int(input("Enter the year to check : "))
if year % 4 == 0 :
    if year % 100 != 0 :
        print("The year ",year," is Leap Year")
    elif year % 400 == 0:
        print("The year ",year," is Leap Year")
    else :
        print("The year ",year," is Not a Leap Year")
else :
        print("The year ",year," is Not a Leap Year")

""" (OTHER WAYS TO DO THIS PROGRAM)
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
    
"""