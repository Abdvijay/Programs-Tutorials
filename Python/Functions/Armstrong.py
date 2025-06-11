def armstrong(num):
    real = num
    sum = 0
    length = len(str(num))
    while num > 0:
        temp = num % 10
        sum = sum + temp ** length
        num = num //10
    
    if real == sum :
        print("The number ",real," is Armstrong Number")
    else:
        print("The number ",real," is Not a Armstrong Number")

number = int(input("Enter the number : "))
armstrong(number)

"""
PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\Functions> python Armstrong.py
Enter the number : 153
The number  153  is Armstrong Number
PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\Functions> python Armstrong.py
Enter the number : 1634
The number  1634  is Armstrong Number
PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\Functions> python Armstrong.py
Enter the number : 154
The number  154  is Not a Armstrong Number

"""