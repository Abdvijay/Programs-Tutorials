number = int(input("Enter the no of elements : "))
elements = []
for i in range(0,number):
    a = int(input(""))
    elements.append(a)
elements.sort()
print("ASC Order : ",elements)
elements.sort(reverse=True)
print("DESC Order : ",elements)

"""
OUTPUT :
        PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\List\List-Programs> python ASC_DESC_List.py
        Enter the no of elements : 5
        1
        3
        4
        2
        5
        ASC Order :  [1, 2, 3, 4, 5]
        DESC Order :  [5, 4, 3, 2, 1]

"""