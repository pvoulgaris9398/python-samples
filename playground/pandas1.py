from datetime import date

import pandas as pd

mydata = {  # type: ignore
    "tickers": ["IBM", "EV", "AAPL", "E"],
    "last_close": [101, 202, 303, 404],
    "volume": [200000, 300000, 4000000, 5500],
}

df = pd.DataFrame(mydata)  # type: ignore

df["price_dt"] = date.today()

print(pd.__version__)
print(df)
