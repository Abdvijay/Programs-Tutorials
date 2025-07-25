names = ['Vijay','Swathi','Laksh']
ages = [24,23,20]

print("List using Zip Function")
list_zipped = list(zip(names,ages))
print(list_zipped)
print(list_zipped[0])
print(list_zipped[1][0])
for name,age in list_zipped:
    print(f'{name}:{age}')

print()
print("Set using Zip Function")
set_zipped = set(zip(names,ages))
print(set_zipped)
for obj in set_zipped:
    print(obj)

print()
print("Dictionary using Zip Function")
dict_zipped = dict(zip(names,ages))
print(dict_zipped)
print(dict_zipped['Vijay'])
for key in dict_zipped:
    print(f'{key} : {dict_zipped[key]}')

print()
print("Tuple using Zip Function")
tup_zipped = tuple(zip(names,ages))
print(tup_zipped)
print(tup_zipped[0])
print(tup_zipped[2][0])
for i in tup_zipped:
    print(i)