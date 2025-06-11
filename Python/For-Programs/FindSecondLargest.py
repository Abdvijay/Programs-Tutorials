from numpy import *
arr = [10,90,23,54,85,47,44]

n = 3

for i in range(1,n+1):
    max = arr[0]
    for j in range(1,len(arr)):
        if max < arr[j] :
            max = arr[j]
    arr.remove(max)
print(max)