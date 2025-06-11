def prime(x):
    for i in range(2,x):
        if x % i == 0 :
            return False
        else :
            return True

number = int(input("Enter the number : "))
bool = prime(number)
if bool :
    print("The number ",number," is Prime Number")
else:
    print("The number ",number," is Not a Prime Number")