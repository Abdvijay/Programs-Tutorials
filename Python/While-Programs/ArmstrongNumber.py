number = int(input("Enter the number : "))
n = number
count = len(str(number))
arms = 0
while n > 0:
    temp = n % 10
    arms = arms + temp ** count
    n = n // 10
if number == arms :
    print("The number ",number," is Armstrong Number")
else:
    print("The number ",number," is Not a Armstrong Number")