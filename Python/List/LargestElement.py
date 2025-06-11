number = int(input("Enter the no of elements : "))
elements = []
for i in range(0,number):
    a = int(input(""))
    elements.append(a)
print("Largest Element : ",max(elements))

'''
OUTPUT:
        PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\List\List-Programs> python SumofElement.py
        Enter the no of elements : 5
        1
        2
        3
        4
        5
        Largest Element : 5
'''