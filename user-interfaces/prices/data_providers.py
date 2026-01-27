import connections
import pandas as pd

"""
To Do:
Add filtering for date range, etc.
"""


def get_prices():
    connection = connections.get_connection()
    df = pd.read_sql(
        "select symbol, open_price, high_price, low_price, close_price, volume, exchange_code_mic, price_dt from pricing.prices;",  # noqa
        connection,
    )
    return df
