# Replaces pattern with a given string.

import re

str = 'This is bad. But sometimes also bad.'

res = re.sub('bad','good',str)
print(res)

# This is good. But sometimes also good.