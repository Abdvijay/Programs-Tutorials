f = open('Ordinary-person.jpg','rb')

f1 = open('testing-pic.jpg','wb')

for i in f:
    f1.write(i)