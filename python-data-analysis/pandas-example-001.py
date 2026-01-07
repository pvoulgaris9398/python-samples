import matplotlib.pyplot as plt  # noqa: F401
import pandas as pd

filename = r"C:\Users\Peter\_work\_tempdata\titanic.csv"

df = pd.read_csv(filename, index_col=0, parse_dates=True)
print(f"Mean Age: {df["Age"].mean()}")
print(f"Median Age, Fare:\n{df[["Age", "Fare"]].mean()}")

print(df.agg({"Age": ["min", "max", "mean", "skew"], "Fare": ["median", "kurtosis"]}))

print(
    df.pivot_table(
        values="value",
        index="location",
        columns="parameter",
        aggfunc="mean",
        margins=True,
    )
)
