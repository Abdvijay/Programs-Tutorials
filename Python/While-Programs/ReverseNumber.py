number = int(input("Enter the number : "))
rev = 0

while number > 0:
    rev = rev * 10 + number % 10
    number = number // 10
print("Rev number is ",rev)