pos = -1
def search(arr,n):
    l = 0
    u = len(arr) - 1
    for i in range(0,len(arr)):
        mid = (l + u) // 2
        if n == arr[mid]:
            globals()['pos'] = mid
            return True
        elif n >= arr[mid]:
            l = mid
        else:
            u = mid
    return False

arr = [43,65,73,11,35,28]
arr.sort()
n = 28

print(arr)

if search(arr,n):
    print("Found at : ",pos)
else:
    print("Not Found")