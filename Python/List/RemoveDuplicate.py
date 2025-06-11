number = int(input("Enter the no of List Elements : "))
list_elements = []
for i in range(0,number):
    a = int(input(""))
    list_elements.append(a)
print("List Elements : ",list_elements)
print("After Remove Duplicate : ",list(set(list_elements)))

"""
OUTPUT :

        PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\List\List-Programs> python RemoveDuplicate.py
        Enter the no of List Elements : 5
        1
        2
        1
        2
        3
        List Elements :  [1, 2, 1, 2, 3]
        After Remove Duplicate :  [1, 2, 3]
"""