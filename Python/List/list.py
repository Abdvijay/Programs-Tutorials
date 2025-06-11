"""
List definition : 
        A list in Python is a built-in data structure used to store an ordered, mutable sequence of items. Lists can hold elements of 
any data type-including strings, numbers, booleans, or even other lists-and allow duplicate values. You define a list using square 
brackets, for example: my_list = ["apple", "banana", "cherry"].

Key characteristics of Python lists:

        1.Ordered: The items have a defined order that does not change unless you modify the list.
        2.You can change, add, or remove items after the list is created.
        3.Allows duplicates: Lists can contain multiple items with the same value.
        4.Flexible data types: A single list can contain elements of different data types, such as integers, strings, and booleans.

Methods : 

append()    -   Adds an element at the end of the list
clear()	    -   Removes all the elements from the list
copy()	    -   Returns a shallow copy of the list
count()	    -   Returns the number of elements with the specified value
extend()	-   Adds all elements of an iterable (e.g., another list) to the end
index()	    -   Returns the index of the first element with the specified value
insert()	-   Inserts an element at a specified position
pop()	    -   Removes and returns the element at the specified position
remove()	-   Removes the first occurrence of the specified value
reverse()	-   Reverses the order of the list in place
sort()	    -   Sorts the list in place

"""

#Creating a list
names = ['vijay','swathi','diya','essai','lakshi']
print(names)

#Print 1st Element
print(names[0])

#Print last Element
print(names[-1])

#Print Length of List
print(len(names))

#It prints from 2nd position
print(names[2:])

#Add element using insert
names.insert(2,10)
print(names)

#Add element using append
names.append(45)
print(names)

#Add more element using extent
names.extend([10,20,30])
print(names)

#Add another list using extend
cars = ['bmw','rolls royce']
names.extend(cars)
print(names)

#Counts the list
print(names.count(10))

#Remove last element using pop
names.pop()
print(names)

#Remove element using remove
names.remove(10)
print(names)

#Remove element using del
del names[5:]
print(names)

#Copy the list from old list
duplicate_list = []
duplicate_list = names.copy()
print(duplicate_list)

#Delete list using del command or you can use clear
# del duplicate_list[:]
# print(duplicate_list)

duplicate_list.clear()
print(duplicate_list)

#Fetch the value index
print(names.index('swathi'))

#Reverse the list
numbers = [1,2,3,4,5]
numbers.reverse()
print(numbers)

#Sort the list
numbers = [4,3,5,2,1]
numbers.sort()
print(numbers)

#Multi types list
multi_list = [1,'Vijay',2.9]
print(multi_list)

#Update a list
print(numbers)
print(numbers.index(2))
numbers[1] = 10
print(numbers)

#Using for loop
print(numbers)
for num in numbers:
    print(num)

#Matrix in list
matrix = [
    [1,2,3],
    ['Vijay','Swathi','Lakshi'],
    ['2.4','5.4','0.4']
]
print(matrix)
print(matrix[2][1])
matrix[1][2] = 'Essai'
print(matrix)

#Min of the list
print(numbers)
print("Min of the list : ",min(numbers))
print("Max of the list : ",max(numbers))
print("Sum of the list : ",sum(numbers))

#Remove duplicate from a list
numbers = [1,2,2,3,3,4,5,5]
print(numbers)
numbers = list(set(numbers))
print(numbers)