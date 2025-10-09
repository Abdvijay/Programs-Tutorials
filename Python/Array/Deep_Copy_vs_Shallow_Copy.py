#Definition:

# 1. Deep copy : 
#     1. It is used copy() function.
#     2. If we update the original array value it cannot reflect at the copied array using copy().

# 2. Shallow copy:
#     1. It is used view() function.
#     2. If we update the original array and shallow copy array it will relfect the other array which means if we update original array
#        it will reflect on copied array or if we update shallow copied array it will relfect the original array.
#     3. This is the diff between shallow copy and deep copy.

from numpy import *

arr1 = array([1,2,3,4,5])
arr2 = array([1,2,3,4,5])

#Deep copy
deep_copy = arr1.copy()
print("Before arr1      : ",arr1)
print("Before deep_copy : ",deep_copy)
arr1[2] = 10
print("After  arr1      : ",arr1)
print("After  deep_copy : ",deep_copy)

print("")

#Shallow copy
shallow_copy = arr2.view()
print("Before arr2         : ",arr2)
print("Before shallow_copy : ",shallow_copy)
arr2[2] = 10
print("After  arr2         : ",arr2)
print("After  shallow_copy : ",shallow_copy) 

print("")

#Value modify for shallow_copy array as well as deep_copy array
shallow_copy[2] = 100
print("Final arr2         : ",arr2)
print("Final shallow_copy : ",shallow_copy)

deep_copy[2] = 100
print("Final arr1         : ",arr1)
print("Final deep_copy    : ",deep_copy)