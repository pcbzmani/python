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
