# pylint: disable=[missing-module-docstring]
import pandas as pd

data = {"name": ["bread", "carrots", "apples"], "price": [101, 202, 303]}

df = pd.DataFrame(data)

print(df.info())
