import re

str = 'i born in 13 11 2000 which is monday'
pattern = r'\d+'

digits = re.findall(pattern,str)
print(digits)

# ['13', '11', '2000']
# \d+ matches one or more digits.
# findall() finds all numbers in the string and gives them as a list: ['13', '11', '2000'].