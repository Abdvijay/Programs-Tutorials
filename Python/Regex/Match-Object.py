import re

str = "this is vijay regex program"
match = re.search("vijay",str)
if match:
    print(f'Matched text : {match.group()}')
    print(f'Matched text start index : {match.start()}')
    print(f'Matched text end index : {match.end()}')

# Matched text : vijay
# Matched text start index : 8
# Matched text end index : 13