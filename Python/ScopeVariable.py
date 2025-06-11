a = 10
print(id(a))
def pr():
    a = 20
    x = globals()['a']
    print(id(x))
    globals()['a'] = 25
    print(a)
pr()
print(a)