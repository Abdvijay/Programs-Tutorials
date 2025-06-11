number = int(input("Enter the number of List Element : "))
list_elements = []
for i in range(0,number):
    a = int(input(""))
    list_elements.append(a)
print("List Elements : ",list_elements)
element = int(input("Enter the element to be search : "))
print("Count is : ",list_elements.count(element))

"""
OUTPUT :
        PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\List\List-Programs> python NoOfOccurence.py
        Enter the number of List Element : 5
        1
        2
        3
        3
        2
        List Elements :  [1, 2, 3, 3, 2]
        Enter the element to be search : 1
        Count is :  1

"""