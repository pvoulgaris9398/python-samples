import pandas as pd
import pyodbc as db


def get_connection_string(env="dev"):
    match env:
        case "prd":
            return "prod-connection-string"
        case "dev":
            return "dev-connection-string"
        case "stg":
            return "stg-connection-string"
        case "uat":
            return "uat-connection-string"
        case "tst":
            return "tst-connection-string"
        case _:
            raise RuntimeError(f"Invalid environment argument: {env}'!")
        # ETC


def test_connection(connection_string):
    try:
        df = pd.read_sql("select @@servername", connection_string)
        print(df.to_string(index=False))
    except db.Error as e:
        print(f"Error connecting to Database: {e}")
    finally:
        print("Closing connection to Database")


if __name__ == "__main__":
    import sys

    try:
        connection_string = None
        match sys.argv:
            case [_, env] if env is not None:
                connection_string = get_connection_string(env)
            case _:
                raise RuntimeError(
                    "Please provide a valid environment name [prd|stg|dev|uat|tst]!"
                )
        test_connection(connection_string)

    except RuntimeError as e:
        print(f"Error: {e}")
    finally:
        print("Exiting...")
