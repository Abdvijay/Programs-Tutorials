from itertools import combinations

items = ['A','B','C']
combo = combinations(items,r=2)
for i in combo:
    print(i)

# ('A', 'B')
# ('A', 'C')
# ('B', 'C')