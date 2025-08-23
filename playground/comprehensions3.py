fruit = ["apple", "oranges", "grapes", "pear", "watermelon", "pineapple"]
lengths = [len(f) for f in fruit]

print(fruit)

print(lengths)


def generateNumbers():
    yield 2 / 2
    yield 3 / 1
    yield 4 / 0
    yield 5 / -1


def generateChildren():
    yield "Alex"
    yield "Arnold"
    yield "Artemis"
    yield "Aaron"
    yield "Archibald"
    yield "Aragorn"


children = generateChildren()

print(next(children))
print(next(children))
print(next(children))
print(next(children))
print(next(children))
print(next(children))

numbersGenerator = generateNumbers()

print("Numbers Generator", numbersGenerator)

try:
    numbers = [n for n in numbersGenerator]
    print("Numbers: ", numbers)
except ZeroDivisionError:
    print("Error!")
