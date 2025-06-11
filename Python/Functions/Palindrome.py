def palindrome(s):
    real = s
    sum = 0
    while s > 0:
        sum = sum * 10 + s % 10
        s = s // 10

    if real == sum :
        print("The number is Palindrome")
    else:
        print("The number is Not a Palindrome")
        
number = int(input("Enter the number : "))
palindrome(number)