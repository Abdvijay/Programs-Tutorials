number = int(input("Enter the number to be check :"))
for i in range(2,number):
    if number % i == 0:
        print("The number ",number," is Not a Prime")
        break
else:
    print("The number ",number," is a Prime")