import connections
import pandas as pd

"""
To Do:
Add filtering for date range, etc.
"""


def get_prices():
    connection = connections.get_connection()
    df = pd.read_sql(
        "select ticker, exchange, price, price_dtm from prices;", connection
    )
    return df
