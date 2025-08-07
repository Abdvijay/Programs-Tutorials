# Returns all matches in a list.
import re

str = "vijay,swathi,lakshi,vijay"
res = re.findall('vijay',str)
print(f'After findall : {res}')

# After findall : ['vijay', 'vijay']