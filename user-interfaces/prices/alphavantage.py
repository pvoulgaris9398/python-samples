import json
import os
import sys

import connections
import file_handling as fh
import json_to_price as jtp
import pandas as pd
import psycopg2  # noqa
import requests as req
from dotenv import load_dotenv
from sqlalchemy import text


def build_request(symbol):
    url = "www.alphavantage.co"
    function = "TIME_SERIES_DAILY"
    """
    "full" is a premium feature. 
    "compact" is the default.
    "compact" returns latest 100 data points
    """
    outputsize = "compact"
    apikey = "demo"
    apikey = os.getenv("ALPHA_VANTAGE_API_KEY")
    return f"https://{url}/query?function={function}&symbol={symbol}&outputsize={outputsize}&apikey={apikey}"


def fetch_data(symbol):
    request = build_request(symbol)
    response = req.get(request)
    response.raise_for_status()
    return response.json()


def save_data(symbol, json_data):
    file_type = "prices"  # todo: generalize to  other types
    file_name = fh.get_file_name(file_type, symbol)
    print(file_name)
    # print(json_data)
    with open(file_name, "w") as json_file:
        json_file.write(json.dumps(json_data, indent=4))


def save_to_database(prices):
    pt = [p.__dict__ for p in prices]
    with connections.get_connection().connect() as connection:
        # Note here we can specify the _names_ of the fields in the dictionary
        # even though they don't agree with the database column names
        inserts = text(
            "insert into pricing.prices(symbol, open_price, high_price, low_price, close_price, volume, price_dt) VALUES (:symbol, :open, :high, :low, :close, :volume, :price_dt)"  # noqa
            # "insert into pricing.prices(symbol, open_price, high_price, low_price, close_price, volume, price_dt) VALUES (?,?,?,?,?,?,?)"  # noqa
        )  # noqa
        connection.execute(inserts, pt)
        connection.commit()


"""
To Do:
- Better error-handling here
- Perhaps return some sort of Optional result
"""


def get_prices_for(symbol, saveToFile=False, saveToDatabase=True):
    try:
        json_data = fetch_data(symbol)

        if saveToFile:
            save_data(symbol, json_data)
        elif saveToDatabase:
            prices = jtp.parse2(json_data)
            save_to_database(prices)
        else:
            print(json.dumps(json_data, indent=4))

        df = pd.json_normalize(json_data)

        return df
    except req.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return pd.DataFrame()


if __name__ == "__main__":
    load_dotenv()

    match sys.argv:
        case [_, symbol]:
            prices = get_prices_for(symbol, False, True)

            # if not prices.empty:
            #    pd.set_option("display.max_columns", None)
            #    print(prices)
        case _:
            print("Please pass symbol on the command-line")
