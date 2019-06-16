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

letters = ["a", "b", "c"]
matrix = [[0, 1], [1, 2]]
zeros = [0] * 5
combined = zeros + letters
num = list(range(5, 20, 2))
char = list("Hello World")
print((char))

numbers = list(range(50))
print(numbers[::-2])


# List unpacking
number = [1, 2, 3, 4, 5, 6, 7]
a, *other, c = number
print(a, c)
print(other)

for index, nums in enumerate(number):
    print(index, nums)

letter = ["a", "b", "c"]
letter.append("d")
letter.insert(0, "-")
letter.pop()
del letter[0: 2]
print(letter)


# Lambda functions

items = [
    ("P1", 18), ("P2", 9), ("P3", 10)
]

items.sort(key=lambda item: item[1])
print(items)


#price = list(map(lambda item: item[1], items))
price = [item[1] for item in items]
print(price)
#price10 = list(filter(lambda item: item[1] >= 10, items))
price10 = [item for item in items if item[1] >= 10]
print(price10)

#Exception
try:
    age = int(input("Enter the Age: "))
except ValueError as ex:
    print("Please enter a valid age")
    print(ex)
    print(type(ex))
else:
    print(f"Age is valid {age} ")


# Class is a blueprint of object
# Object is an instance of class

# Ex: Class - Human, Object - John, Mani


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    @classmethod
    def zero(cls):
        cls(0, 0)

    def draw(self):
        print(f"Point ({self.x},{self.y})")


point = Point(1, 50)
other = Point(1, 50)
another = Point(0, 25)
print(point == other)
print(point > another)
print(Point.zero())
point.draw()


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
