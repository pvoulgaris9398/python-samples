squares1 = [x * x for x in range(10)]

print(squares1)

squares2 = [x * x for x in range(10) if x % 2 == 1]

print(squares2)

coords = [(x, y) for x in range(4) for y in range(4)]

print(coords)
