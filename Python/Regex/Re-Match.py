# Matches only at the beginning of the string. Otherwise it returns None

import re

str = "This is regex program match function"

sub_str = re.match(r'This',str)
print(sub_str)

# <re.Match object; span=(0, 4), match='This'>