number = int(input("Enter the no of List Elements : "))
list_elements = []
for i in range(0,number):
    a = int(input(""))
    list_elements.append(a)
print("List Elements : ",list_elements)
print("Reverse List : ",list_elements[::-1])

"""
OUTPUT :

        PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\List\List-Programs> python ReverseAList.py
        Enter the no of List Elements : 5
        1
        2
        3
        4
        5
        List Elements :  [1, 2, 3, 4, 5]
        Reverse List :  [5, 4, 3, 2, 1]

"""