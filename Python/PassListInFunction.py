def count(lst):
    ltrcount = 0
    for i in lst:
        ct = 0
        ct = len(i)
        if ct >= 5:
            ltrcount = ltrcount + 1
    return ltrcount

lst = ['vj','swathi','essaiyamuthu','Lakshi']
result = count(lst)
print("Letters 5 more than is : {}".format(result))