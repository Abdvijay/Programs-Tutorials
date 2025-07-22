from functools import reduce
lst = [1,2,4,5,6,7,8,9]

print("Original list : ",lst)

even = list(filter(lambda n : n % 2 == 0,lst))

print("Filter used : ",even)

doubles = list(map(lambda n : n * 2,even))

print("Map used : ",doubles)

sums = reduce(lambda a,b: a+b,doubles)

print("Reduce used : ",sums)

'''

Original list :  [1, 2, 4, 5, 6, 7, 8, 9]
Filter used :  [2, 4, 6, 8]
Map used :  [4, 8, 12, 16]
Reduce used :  40

'''