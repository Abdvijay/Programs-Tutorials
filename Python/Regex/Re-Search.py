# Searches for the first match anywhere in the string.

import re

str = "This is my code"

sub_str = re.search("is",str)
print(sub_str)

sub = re.search("aa",str)
print(sub)

# <re.Match object; span=(2, 4), match='is'>
# None