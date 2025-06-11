rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(65, 65 + i):
        print(chr(j), end="")
    print()

"""
rows = 5
for i in range(1,rows+1):
    for j in range(1,rows-i + 1):
        print("",end=" ")
    for ch in range(65,65 + i):
        print(chr(ch), end="")
    print("")

    A
   AB
  ABC
 ABCD
ABCDE

"""