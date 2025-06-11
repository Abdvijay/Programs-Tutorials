from numpy import *

arr = array([
    [1,2,3],
    [7,8,9],
    [3,4,5]
])

m = matrix(arr)
m1 = matrix('1 2 3; 4 5 6; 1 4 3')
print(m)
print("max of mat : ",m.max())
print("min of mat : ",m.min())
print(diagonal(m))
print("Addition of mat : \n",m+m1)
print("Multiply of mat : \n",m*m1)