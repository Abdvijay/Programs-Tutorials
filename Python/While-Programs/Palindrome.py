number = int(input("Enter the number : "))
n,sum = number,0
while n > 0:
    sum = sum * 10 + n % 10
    n = n // 10

if sum == number :
    print("The number ",number," is Palindrome")
else:
    print("The number ",number," is Not a Palindrome")