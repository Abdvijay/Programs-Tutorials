a = 10
print(a)
print(type(a))
"10"
"<class 'int'>"

b = 9.2
print(b)
print(type(b))
"9.2"
"<class 'float'>"

c = 5 + 9j
print(c)
print(type(c))
"5 + 9j"
"<class 'complex'>"

d = True
print(d)
print(type(d))
"True"
"<class 'bool'>"

print(int(True))
print(int(False))
"1"
"0"

var = complex(5,5)
print(var)
print(type(var))
"(5+5j)"
"<class 'complex'>"

lst = [ 1,2,3,4,5 ]
print(type(lst))
"<class 'list'>"

sets = { 1,2,3,4,5}
print(type(sets))
"<class 'set'>"

tup = (1,2,3,4,5)
print(type(tup))
"<class 'tuple'>"

dic = {"key" : "Value"}
print(type(dic))
"<class 'dict'>"

str = "Vijay"
print(type(str))
"<class 'str'>"

print(list(range(0,10)))
"[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"

rang = range(0,12,2)
print(list(rang))
print(type(rang))
"[0, 2, 4, 6, 8, 10]"
"<class 'range'>"

print(list(range(1,20,2)))
"[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]"

print(list(range(0,33,3)))
"[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]"