# Using Itertools Takewhile
from itertools import takewhile

numbers = [-1,-2,-3,0,1,2,3]
non_neg = takewhile(lambda x: x < 0, numbers)
print(list(non_neg))