import json
import os

import file_handling as fh
import pandas as pd
import requests as req
from dotenv import load_dotenv


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


"""
To Do:
- Better error-handling here
- Perhaps return some sort of Optional result
"""

def json_to_price(json):
    

def get_prices_for(symbol, save=False):
    try:
        json_data = fetch_data(symbol)

        if save:
            save_data(symbol, json_data)
        else:
            print(json.dumps(json_data, indent=4))

        df = pd.json_normalize(json_data)

        return df
    except req.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return pd.DataFrame()


if __name__ == "__main__":
    load_dotenv()

    prices = get_prices_for("EV", True)

    if not prices.empty:
        pd.set_option("display.max_columns", None)
        print(prices)
