import pandas as pd

calories = {"day1": 1000, "day2": 2500, "day3": 2750, "day4": 2277}

a = pd.Series(calories)

print(a)

print(a.loc["day2"])
