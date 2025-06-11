number = int(input("Enter the number : "))
n = len(str(number))

new = 0
num = number
while num > 0:
    temp = num % 10
    new = new + temp ** n
    num = num // 10

if number == new :
    print("The given number is Armstrong Number")
else:
    print("The given number is not a Armstrong Number")
"""

PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\If-Else-Programs> python ArmstongNumber.py
Enter the number : 153
The given number is Armstrong Number

PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\If-Else-Programs> python ArmstongNumber.py
Enter the number : 1634
The given number is Armstrong Number

PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\If-Else-Programs> python ArmstongNumber.py
Enter the number : 370
The given number is Armstrong Number

PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\If-Else-Programs> python ArmstongNumber.py
Enter the number : 65
The given number is not a Armstrong Number

"""