av = 5
n = int(input("How many candies you want ? "))
for i in range(1,n+1):
    if (i > av) :
        print("Out of stock")
        break
    print("Candy")
print("Thanks for purchase!!!")