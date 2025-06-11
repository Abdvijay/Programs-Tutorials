my_tuple = (1,2,3,2,4,5)
number = int(input("Enter the number : "))
if number in my_tuple:
    print(my_tuple.count(number))
else:
    print("Number not exits in the tuple")

'''
OUTPUT : 
        PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\Tuples\Tuple-Programs> python CountValues.py    
        Enter the number : 2
        2
        PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\Tuples\Tuple-Programs> python CountValues.py
        Enter the number : 1
        1
'''