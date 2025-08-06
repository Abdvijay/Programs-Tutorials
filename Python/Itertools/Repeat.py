from itertools import repeat

lst = [1,2,3,4]
for i in repeat(lst,4):
    print(i)

# [1, 2, 3, 4]
# [1, 2, 3, 4]
# [1, 2, 3, 4]
# [1, 2, 3, 4]