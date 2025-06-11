from numpy import *

arr = array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12]
])

print(arr)


arr1 = arr.flatten()
print(arr1)

arr2 = arr1.reshape(4,3)
print(arr2)

arr3 = arr1.reshape(2,2,3)
print(arr3)