"""
Definition :
            A dictionary in Python is a collection of key-value pairs.
            Each key is unique, and it's used to access its corresponding value.


| Method          | Description                                         | Example Output                           |
| --------------- | --------------------------------------------------- | ---------------------------------------- |
| `dict.get(key)` | Returns the value for the key, or `None` if missing | `my_dict.get("age") → 25`                |
| `dict.keys()`   | Returns all keys in the dictionary                  | `dict_keys(['name', 'age', 'city'])`     |
| `dict.values()` | Returns all values                                  | `dict_values(['Alice', 25, 'New York'])` |
| `dict.items()`  | Returns all key-value pairs as tuples               | `[('name', 'Alice'), ('age', 25)]`       |
| `dict.update()` | Adds or updates key-value pairs                     | `my_dict.update({"age": 30})`            |
| `dict.pop(key)` | Removes a key and returns its value                 | `my_dict.pop("city") → 'New York'`       |
| `dict.clear()`  | Removes all items                                   | `{}`                                     |
| `key in dict`   | Checks if key exists                                | `"name" in my_dict → True`               |
| `len(dict)`     | Number of items in dictionary                       | `len(my_dict) → 3`                       |
| `dict.copy()`   | Returns a shallow copy of the dictionary            | `new_dict = my_dict.copy()`              |


"""


my_dictionary = {1:"Vijay",2:"Swathi",3:"Essai",4:"Diya"}
print(my_dictionary)
"{1: 'Vijay', 2: 'Swathi', 3: 'Essai', 4: 'Diya'}"

my_dict = {"Vijay":"Python","Swathi":"Medical-Coding","Essai":"Java","Diya":"C++"}
print(my_dict)
"{'Vijay': 'Python', 'Swathi': 'Medical-Coding', 'Essai': 'Java', 'Diya': 'C++'}"

print(my_dict.get("Vijay"))
print(my_dict["Essai"])
"Python"
"Java"

print(my_dict.pop("Diya"))
print(my_dict)
"C++"
"{'Vijay': 'Python', 'Swathi': 'Medical-Coding', 'Essai': 'Java'}"

my_dict["Diya"] = "C-Sharp"
print(my_dict)
"{'Vijay': 'Python', 'Swathi': 'Medical-Coding', 'Essai': 'Java', 'Diya': 'C-Sharp'}"

my_dict["Diya"] = "C++"
print(my_dict)
"{'Vijay': 'Python', 'Swathi': 'Medical-Coding', 'Essai': 'Java', 'Diya': 'C++'}"

print(my_dict.values())
"dict_values(['Python', 'Medical-Coding', 'Java', 'C++'])"

print(my_dict)
my_dict.update({"Diya":"C-Sharp"})
print(my_dict)
"{'Vijay': 'Python', 'Swathi': 'Medical-Coding', 'Essai': 'Java', 'Diya': 'C++'}"
"{'Vijay': 'Python', 'Swathi': 'Medical-Coding', 'Essai': 'Java', 'Diya': 'C-Sharp'}"

print(my_dict)
my_dict.update({"Lakshi" : "MySql"})
print(my_dict)
"{'Vijay': 'Python', 'Swathi': 'Medical-Coding', 'Essai': 'Java', 'Diya': 'C-Sharp'}"
"{'Vijay': 'Python', 'Swathi': 'Medical-Coding', 'Essai': 'Java', 'Diya': 'C-Sharp', 'Lakshi': 'MySql'}"

new_dict = {"Python":["PyCharm","Sublime"],"Java":{"Enterprise":"JetBeans","Normal":"Eclipse"}}
print(new_dict)
"{'Python': ['PyCharm', 'Sublime'], 'Java': {'Enterprise': 'JetBeans', 'Normal': 'Eclipse'}}"

print(new_dict["Python"])
"['PyCharm', 'Sublime']"

print(new_dict["Java"]["Enterprise"])
"JetBeans"

new_dict.popitem()
print(new_dict)
"'Python': ['PyCharm', 'Sublime']}"

print(my_dict)
print(my_dict["Vijay"])
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

