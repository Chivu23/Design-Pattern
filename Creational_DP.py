"""
Example:
CREATION Design Patterns
___SINGLETON___
"""


# creating a single instance of a class

class SingletonClass:
    __instance = None

    sector = "IT"  # attribute of a class

    def __init__(self, name):  # define constractor with one parameter or 0. name = parameter
        self.name = name

    def __new__(cls, *args, **kwargs):  # cls = reference to class
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance


obj1 = SingletonClass("WeAreTheOne")
print(obj1.name)
print(obj1.sector)
print(obj1)
print(id(obj1))

obj2 = SingletonClass("MichelJackson")
print(obj2.name)
print(obj2.sector)
print(obj2)
print(id(obj2))

# the same memory address & id

print(obj1.name)  # overwritten object values
