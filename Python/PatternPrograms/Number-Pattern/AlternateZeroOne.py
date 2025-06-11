rows = 5
for i in range(rows+1):
    for j in range(i):
        print((i + j)% 2,end="")
    print()

"""
1
01
101
0101
10101

"""