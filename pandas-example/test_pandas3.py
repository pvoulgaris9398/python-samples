import pandas as pd

df1 = pd.read_csv("test1.csv", sep="|", index_col=False)
df2 = pd.read_csv("test2.csv", sep="|", index_col=False)

merged_df = pd.merge(df1, df2, on="RECORD_ID", how="outer", indicator=True)

# diff_df = df1.compare(df2, keep_shape=True)

print(merged_df)
