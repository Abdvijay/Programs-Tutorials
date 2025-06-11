pos = -1

def LinearSearch(lst,n):
    for i in range(0,len(lst)):
        if lst[i] == n:
            globals()['pos'] = i
            return True
    return False

lst = [1,5,3,7,8,5]
n = 5
if LinearSearch(lst,n):
    print("Found at : ",pos)
else:
    print("Not Found")