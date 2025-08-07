# Splits the string by the given pattern, just like str.split() but using regex rules.

import re

str = "vijay, swathi; lakshi_essai.dhiya deeksha"
pattern = r'[ ;.,_]+'

res = re.split(pattern,str)
print(res)


# [ ,;]+ means: split on any combination of space, comma, or semicolon.
# You get clean parts of the text.
# ['vijay', 'swathi', 'lakshi', 'essai', 'dhiya', 'deeksha']