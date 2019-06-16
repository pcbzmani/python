# python
Python Basics
# Variables

# String
py_string = "Hello World"
py_string = 'Hello World'

# Boolen
py_boolen = True
py_boolen = False

# integer
py_int = 56

# float

py_float = 56.3


# Inheritance
class Human:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Class Human is a base class
# Class Male , female is sub-class


class Male(Human):
    def __init__(self):
        self.weight = 2
        super().__init__()

    def sex(self):
        print("Male")


class Female(Human):
    def sex(self):
        print("female")


john = Male()
john.eat()
print(john.weight)
# All class inherit from 'object class'
print(isinstance(john, Human))
print(issubclass(Female, Human))
