list = [1,2,3,4,5,6,7,8,9,10]
list1, list2= [], []
mid  = len(list) // 2

for i in range(0,len(list)):
    if i < mid:
        list1.append(list[i])
    else:
        list2.append(list[i])

print(list)
print(list1)
print(list2)