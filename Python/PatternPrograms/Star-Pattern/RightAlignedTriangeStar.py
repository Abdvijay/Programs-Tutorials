rows = 5
for i in range(1,rows+1):
    loop = rows-i
    for j in range(1,loop+1):
        print(" ",end="")
    print("*" * i)

''' 
rows = 5
for i in range(1,rows+1):
    print(" " * (rows - i) , "*" * i)

OUTPUT :

     *
    **
   ***
  ****
 *****

'''
