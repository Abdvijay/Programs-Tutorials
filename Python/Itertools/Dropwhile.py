from itertools import dropwhile

# Using normal method 
numbers = [-1,-2,-3,0,1,2,3]
non_neg = []
for i in numbers:
    if i >= 0 :
        non_neg.append(i)
print(non_neg)

# Using List Comprehension
numbers = [-1,-2,-3,0,1,2,3]
non_neg = [i for i in numbers if i >= 0]
print(non_neg)

# Using Itertools Dropwhile
numbers = [-1,-2,-3,0,1,2,3]
non_neg = dropwhile(lambda x: x < 0, numbers)
print(list(non_neg))