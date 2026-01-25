#!/usr/bin/env python3

import json

import json_to_price as jtp

json_data = """{
    "Meta Data": {
        "1. Information": "Daily Prices (open, high, low, close) and Volumes",
        "2. Symbol": "IBM",
        "3. Last Refreshed": "2026-01-23",
        "4. Output Size": "Compact",
        "5. Time Zone": "US/Eastern"
    },
    "Time Series (Daily)": {
        "2026-01-23": {
            "1. open": "294.0700",
            "2. high": "294.3350",
            "3. low": "289.7900",
            "4. close": "292.4400",
            "5. volume": "3298424"
        },
        "2026-01-22": {
            "1. open": "299.4200",
            "2. high": "300.9300",
            "3. low": "293.5300",
            "4. close": "294.6700",
            "5. volume": "3670152"
        }
    }
}"""

if __name__ == "__main__":
    df = jtp.parse(json.loads(json_data))
    print(df)
