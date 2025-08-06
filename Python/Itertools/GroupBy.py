from itertools import groupby

items = [1,1,2,3,3,3,4,4,5,5]
grb = groupby(items)
for i,key in grb:
    print(i,list(key))


# 1 [1, 1]
# 2 [2]
# 3 [3, 3, 3]
# 4 [4, 4]
# 5 [5, 5]