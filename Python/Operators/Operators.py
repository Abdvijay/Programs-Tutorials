x = 2
y = 3
print(list[x+y,x-y,x*y,x/y,x//y,x%y])
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)

"list[5, -1, 6, 0.6666666666666666, 0, 2]"

[a,b] = [5,6]
print(a,b)
"5 6"

x += a
print(x)
"7"

x *= 3
print(x)
"21"

n = 7
print(n)
print(-n)
"7"
"-7"
n = -n
print(n)
"-7"

a = 5
b = 5
print(list([a < b, a > b, a <= b, a >= b, a == b, a != b]))
"[False, False, True, True, True, False]"

print(a <=5 and b > 10)
"False"

print( a ==5 and b == 5)
"True"

print( a >= 6 or b == 5)
"True"

x = True
print(not x)
"False"