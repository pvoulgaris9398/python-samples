import datetime as dt

import pandas as pd

df1 = pd.read_csv("test1.csv", sep="|", index_col=False)
df2 = pd.read_csv("test2.csv", sep="|", index_col=False)

df1["parse_start_date"] = dt.date.today()
df2["parse_start_date"] = dt.date.today()

ds1 = set([tuple(values) for values in df1.values.tolist()])
ds2 = set([tuple(values) for values in df2.values.tolist()])

ds1.symmetric_difference(df2)

# print(pd.DataFrame(list(ds1.difference(ds2))))
# print(pd.DataFrame(list(ds2.difference(ds1))))

print(df1.describe())

print(df1.info())
