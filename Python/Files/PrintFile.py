with open('Python\Files\sample.txt', 'r') as file:
    content = file.read()
    print(content)

with open('Python\Files\sample.txt', 'r') as file:
    content = file.readlines()
    print(content)

"""
Hi this is Vijay
MCA Student
Nellaiyans

['Hi this is Vijay\n', 'MCA Student\n', 'Nellaiyans']

"""