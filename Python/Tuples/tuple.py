"""
Definition : 
            In Python, a tuple is a collection of items that is ordered and immutable (i.e., you can't change its contents after creation).

Key Features:
            1.Ordered → Elements have a fixed position.
            2.Immutable → Cannot be changed after creation.
            3.Allows duplicates.
            4.Can hold elements of different types (e.g., integers, strings, etc.)
            5.You can access element using [] with the position.

"""

my_tuple = (10,28,80,15,15)
print(my_tuple)

'(10, 28, 80, 15, 15)'

tup = (10,2.3,'Vijay')
print(tup)
"(10, 2.3, 'Vijay')"

print(my_tuple.index(28))
'1'

print(my_tuple.count(15))
'2'

numbers = (10,20,30,40,50)
print(numbers[2])
'30'