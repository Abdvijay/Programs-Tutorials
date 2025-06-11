number = int(input("Enter the no of elements : "))
elements = []
for i in range(0,number):
    a = int(input(""))
    elements.append(a)
print(elements)
for i in range(0,number+1):
    if i % 2 != 0 :
        elements.remove(i)
print(elements)

"""
OUTPUT:
        PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\List\List-Programs> python RemoveOddElement.py
        Enter the no of elements : 5
        1
        2
        3
        4
        5
        [1, 2, 3, 4, 5]
        [2, 4]

"""