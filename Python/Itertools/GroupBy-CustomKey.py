from itertools import groupby

students = [
    {'name' : 'Vijay', 'age' : 24},
    {'name' : 'Swathi', 'age' : 23},
    {'name' : 'Laksh', 'age' : 19},
    {'name' : 'Dhiya', 'age' : 23},
    {'name' : 'Essai', 'age' : 24}
]

students.sort(key= lambda x : x['age'])
g_data = groupby(students, key= lambda x : x['age'])
for key, group in g_data:
    print(f' Age {key} Group -> {list(group)}')

#  Age 19 Group -> [{'name': 'Laksh', 'age': 19}]
#  Age 23 Group -> [{'name': 'Swathi', 'age': 23}, {'name': 'Dhiya', 'age': 23}]
#  Age 24 Group -> [{'name': 'Vijay', 'age': 24}, {'name': 'Essai', 'age': 24}]