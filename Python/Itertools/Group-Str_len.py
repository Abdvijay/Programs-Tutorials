from itertools import groupby

items = ['Vijay','Swathi','Lakshitha','Dhiya','Essai']
sort_items = sorted(items,key=lambda x : len(x))
g_data = groupby(sort_items,key = lambda x: len(x))

for key, group in g_data:
    print(f'Group : {key} -> {list(group)}')

# Group : 5 -> ['Vijay', 'Dhiya', 'Essai']
# Group : 6 -> ['Swathi']
# Group : 9 -> ['Lakshitha']