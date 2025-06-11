from functools import reduce

lst = [1,2,3,4,5,6,7,8,9,10]

result = list(filter(lambda n : n % 2 == 0,lst))
print(result)
double = list(map(lambda n : n * 2,result))
print(double)
sum = reduce(lambda a, b : a+b,double)
print(sum)