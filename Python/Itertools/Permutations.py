from itertools import permutations

items = ['A','B','C']
perm = permutations(items,r=2)
print(perm)
for i in perm:
    print(i)

# ('A', 'B')
# ('A', 'C')
# ('B', 'A')
# ('B', 'C')
# ('C', 'A')
# ('C', 'B')