from numpy import *
arr = array([1,9,3,7,5])
arr = sorted(arr)
max = arr[0]
temp = max
for i in range(1,len(arr)):
    if arr[i] > max:
        temp = max
        max = arr[i]
print("Max : ",max)
print("Second : ",temp)