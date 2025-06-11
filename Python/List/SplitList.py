number = int(input("Enter the number of List Elements : "))
elements = []
for i in range(0,number):
    a = int(input(""))
    elements.append(a)
mid = len(elements) // 2
print("Full Elements : ",elements)
print("1st Half Elements : ",elements[:mid])
print("2nd Half Elements : ",elements[mid:])

"""
OUTPUT : 
        PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\List\List-Programs> python SplitList.py
        Enter the number of List Elements : 5
        1
        2
        3
        4
        5
        Full Elements :  [1, 2, 3, 4, 5]
        1st Half Elements :  [1, 2]
        2nd Half Elements :  [3, 4, 5]

"""