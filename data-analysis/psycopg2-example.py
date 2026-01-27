import os

import pandas as pd
import psycopg2


def test2():
    host = os.getenv("DBSERVER")
    dbname = os.getenv("DBNAME")
    user = os.getenv("DEVUSERNAME")
    password = os.getenv("DEVUSERPASSWORD")
    port = os.getenv("DBPORT")  # noqa
    connection_string = (
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
    )

    connection_string_2 = (
        f"host='{host}' dbname='{dbname}' user='{user}' password='{password}'"
    )

    connection = psycopg2.connect(connection_string_2)
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO pricing.prices (symbol, open_price, high_price, low_price, close_price, volume, price_dt) VALUES (%s, %s, %s, %s, %s, %s,%s)",  # noqa
        ("AAPL", 101, 105, 98, 102, 606067, "1/26/2026"),
    )

    connection.commit()
    cursor.close()
    connection.close()

    df = pd.read_sql("select * from prices", connection_string)
    print(df)


def test1():
    host = os.getenv("DBSERVER")
    dbname = os.getenv("DBNAME")
    user = os.getenv("DEVUSERNAME")
    password = os.getenv("DEVUSERPASSWORD")
    port = os.getenv("DBPORT")  # noqa
    connection_string = (
        f"host='{host}' dbname='{dbname}' user='{user}' password='{password}'"
    )
    connection = psycopg2.connect(connection_string)

    cursor = connection.cursor()

    cursor.execute("select * from prices")

    records = cursor.fetchall()

    print(records)


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()

    test2()
