'''
Definition :
            A set is a collection of unique, unordered elements. It is built-in to Python and is useful when you want to:
            Remove duplicates
            Perform mathematical set operations (like union, intersection, etc.)
            It is defined using curly braces {} or the set() function.

'''

my_set = {1,2,4,5,3}
print(my_set)
'{1, 2, 3, 4, 5}'

my_set = {1,3,2,5,5}
print(my_set)
'{1, 2, 3, 5}'

my_set.add(10)
print(my_set)
'{1, 2, 3, 5, 10}'

my_set.pop()
print(my_set)
'{2, 3, 5, 10}'

my_set.pop()
print(my_set)
'{3, 5, 10}'

new_set = my_set.copy()
print(new_set)
'{10, 3, 5}'

my_set.clear()
print(my_set)
'set()'

new_set.update(['vijay','swathi'])
print(new_set)
"{3, 5, 10, 'swathi', 'vijay'}"

new_set.remove(10)
print(new_set)
"{3, 'swathi', 5, 'vijay'}"

new_set.remove(4)
print(new_set)
'''Traceback (most recent call last):
  File "c:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\Set\Introduction\set.py", line 37, in <module>
    new_set.remove(4)
KeyError: 4'''

new_set.discard(4)
print(new_set)
"{3, 5, 'swathi', 'vijay'}"

"Note : If we remove un exists element using remove it retuns error but if you using discard it doesnot return error instead it returns the set"