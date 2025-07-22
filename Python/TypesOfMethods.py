'''
| Method Type         | Decorator Used   | Can Access                                    | Common Use                                |
| ------------------- | ---------------- | --------------------------------------------- | ----------------------------------------- |
| **Instance Method** | *(no decorator)* | `self` (instance variables & class variables) | Operate on individual object data         |
| **Class Method**    | `@classmethod`   | `cls` (only class variables)                  | Factory methods, modifying class state    |
| **Static Method**   | `@staticmethod`  | ❌ (no access to instance/class data)          | Utility/helper functions related to class |


'''


class Student:
    college = "ABC College"  # class variable

    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instance method
    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # Class method
    @classmethod
    def get_college(cls):
        return cls.college

    # Static method
    @staticmethod
    def info():
        print("This is a Student class for managing marks.")

s1 = Student("Vijay", 85, 90, 95)

print("Average:", s1.average())            # Instance method
print("College:", Student.get_college())   # Class method
Student.info()                              # Static method