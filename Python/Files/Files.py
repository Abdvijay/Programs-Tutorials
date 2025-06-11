f = open('sample.txt','r')

f1 = open('testing.txt','w')
for i in f:
    f1.write(i)