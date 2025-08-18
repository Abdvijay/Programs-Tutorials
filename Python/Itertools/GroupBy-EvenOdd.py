from itertools import groupby

items = [2,4,6,7,8,10,11,12,13]

g_data = groupby(items, key = lambda x: 'Even' if x % 2 == 0 else 'Odd')

for key, group in g_data:
    print(f'Group : {key} -> {list(group)}')

# Group : Even -> [2, 4, 6]
# Group : Odd -> [7]
# Group : Even -> [8, 10]
# Group : Odd -> [11]
# Group : Even -> [12]
# Group : Odd -> [13]