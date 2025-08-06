from itertools import product

colors = ['R','G','B']
size = ['S','M','L']

prod = product(colors,size)
print(prod)
for i in prod:
    print(i)

# ('R', 'S')
# ('R', 'M')
# ('R', 'L')
# ('G', 'S')
# ('G', 'M')
# ('G', 'L')
# ('B', 'S')
# ('B', 'M')
# ('B', 'L')