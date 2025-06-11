num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
op = input("Enter the operator('+,-,*,/,%) one of them : ")

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
else:
    print(num1 % num2)

"""
PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\If-Else-Programs> python SimpleCalculator.py 
Enter 1st Number : 4
Enter 2nd Number : 5
Enter the operator('+,-,*,/,%) one of them : +
9
PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\If-Else-Programs> python SimpleCalculator.py
Enter 1st Number : 5
Enter 2nd Number : 7
Enter the operator('+,-,*,/,%) one of them : %
5

"""