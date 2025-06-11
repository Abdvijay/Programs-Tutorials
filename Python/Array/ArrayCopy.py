from array import *
vals = array('i',[1,2,3,4,5])

newArr = array(vals.typecode,(a * a for a in vals))
for i in newArr:
    print(i)

arr = array(newArr.typecode,[])
for a in newArr:
    arr.append(a)

print(arr)

print(arr.count(1))
arr.extend([36,49,64,81,100])
print(arr)

print(arr.typecode)