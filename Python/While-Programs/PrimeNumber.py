number = int(input("Enter the number : "))
i = 2
flag = False
while i <= number:
    if number % i == 0 :
        flag = True
    i = i + 1
if(flag):
    print("The number ",number," is Prime Number")
else:
    print("The number ",number," is Not a Prime Number")