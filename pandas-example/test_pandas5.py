import pandas as pd

data1 = {
    "RECORD_ID": [3, 2, 1, 4, 0],
    "FIELD1": ["a", "b", "c", "z", "e"],
    "FIELD2": ["a", "b", "c", "z", "e"],
}
data2 = {
    "RECORD_ID": [5, 2, 1, 4, 7],
    "FIELD1": ["a", "b", "x", "d", "e"],
    "FIELD2": ["a", "b", "x", "z", "e"],
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

found1 = df1[df1["RECORD_ID"].isin(df2["RECORD_ID"])]
print(found1)
found2 = df2[df2["RECORD_ID"].isin(df1["RECORD_ID"])]
print(found2)

diff = found1.compare(found2)

print(diff)
