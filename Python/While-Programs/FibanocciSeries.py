n = int(input("Enter the number : "))
f1,f2,i = 0,1,2
print(f1,f2, end=" ")
while i < n:
    f3,f1,i = f1+f2,f2,i+1
    f2 = f3
    print(f3,end=" ")
 