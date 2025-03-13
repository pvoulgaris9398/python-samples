import datetime as dt

import pandas as pd

df1 = pd.read_csv("test1.csv", sep="|", index_col=False)
df2 = pd.read_csv("test2.csv", sep="|", index_col=False)

df1["parse_start_date"] = dt.date.today()
df2["parse_start_date"] = dt.date.today()

diff_df = df1.compare(df2, keep_shape=True)

print(diff_df)
