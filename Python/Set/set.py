'''
Definition :
            A set is a collection of unique, unordered elements. It is built-in to Python and is useful when you want to:
            Remove duplicates
            Perform mathematical set operations (like union, intersection, etc.)
            It is defined using curly braces {} or the set() function.


            | **Method**                        | **Description**                           | **Example Output**                |
| --------------------------------- | ----------------------------------------- | --------------------------------- |
| `add(x)`                          | Adds element `x` to the set               | `{1, 2} → add(3) → {1, 2, 3}`     |
| `update(iterable)`                | Adds multiple elements                    | `{1} → update([2,3]) → {1, 2, 3}` |
| `remove(x)`                       | Removes `x` (error if not found)          | `{1, 2} → remove(1) → {2}`        |
| `discard(x)`                      | Removes `x` (no error if not found)       | `{1, 2} → discard(3) → {1, 2}`    |
| `pop()`                           | Removes random element                    | `{1, 2, 3} → pop() → {2, 3}`      |
| `clear()`                         | Removes all elements                      | `{1, 2} → clear() → set()`        |
| `union(s2)`                       | Returns all unique elements               | `{1,2} ∪ {2,3} → {1,2,3}`         |
| `intersection(s2)`                | Common elements                           | `{1,2,3} ∩ {2,3,4} → {2, 3}`      |
| `difference(s2)`                  | Elements only in first set                | `{1,2,3} - {2,3} → {1}`           |
| `symmetric_difference(s2)`        | Elements in either but not both           | `{1,2} ⊕ {2,3} → {1, 3}`          |
| `intersection_update(s2)`         | Keeps only common elements (in-place)     | `{1,2,3} ∩= {2,3} → {2, 3}`       |
| `difference_update(s2)`           | Removes elements in second set (in-place) | `{1,2,3} -= {2} → {1, 3}`         |
| `symmetric_difference_update(s2)` | Updates with symmetric diff (in-place)    | `{1,2} ⊕= {2,3} → {1, 3}`         |
| `issubset(s2)`                    | True if all elements in set exist in `s2` | `{1,2} ⊆ {1,2,3} → True`          |
| `issuperset(s2)`                  | True if set contains all of `s2`          | `{1,2,3} ⊇ {1,2} → True`          |
| `isdisjoint(s2)`                  | True if no common elements                | `{1,2} ∩ {3,4} → True`            |

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