from array import *

arr = array('i',[])
n = int(input("Enter the length of an array : "))
for i in range(n):
    x = int(input("Enter the value : "))
    arr.append(x)
print((arr))

search = int(input("Enter the search element :"))
count = 0
for i in range(0,n):
    if search == arr[i]:
        count = i
        break
print("Position of ",search," is : ",count)