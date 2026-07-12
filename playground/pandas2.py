import pandas as pd

a = range(0, 100)

b = [x * x for x in a if x % 2 == 0]
c = [f"Index = [{x}]" for x in a if x % 2 == 0]
print(c)
dt = pd.Series(b, index=c)

print(dt)
