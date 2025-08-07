# Returns an iterator of match objects, not strings. You can extract start position, end position, and group value.

import re

str = 'i born in 13 11 2000 which is monday'
pattern = r'\d+'

res = re.finditer(pattern,str)
for i in res:
    print(f'Value : {i.group()} , Start at : {i.start()} , End at : {i.end()}')


# Value : 13 , Start at : 10 , End at : 12
# Value : 11 , Start at : 13 , End at : 15
# Value : 2000 , Start at : 16 , End at : 20
# match.group() gives the matched value.
# match.start() and match.end() give the position.
# Use this if you're doing advanced processing.