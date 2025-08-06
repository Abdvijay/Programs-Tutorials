from itertools import groupby

items = [2,4,6,7,8,10,11,12,13]

g_data = groupby(items, key = lambda x: 'Even' if x % 2 == 0 else 'Odd')

for key, group in g_data:
    print(f'Group : {key} -> {list(group)}')