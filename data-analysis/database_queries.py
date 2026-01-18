import pandas as pd
from sqlalchemy import create_engine


def get_connection(env="dev"):
    match env:
        case "prd":
            return "prod-connection-string"
        case "dev":
            host = "todo"
            dbname = "todo"
            user = "todo"
            password = "todo"
            port = 5432
            return create_engine(
                f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
            )

        case "stg":
            return "stg-connection-string"
        case "uat":
            return "uat-connection-string"
        case "tst":
            return "tst-connection-string"
        case _:
            raise RuntimeError(f"Invalid environment argument: {env}'!")
        # ETC


def test_connection(connection):
    try:
        df = pd.read_sql("select version();", connection)
        print(df.to_string(index=False))
    except Exception as e:
        print(f"Error connecting to Database: {e}")
    finally:
        print("Closing connection to Database")


if __name__ == "__main__":
    import sys

    try:
        connection = None
        match sys.argv:
            case [_, env] if env is not None:
                connection = get_connection(env)
            case _:
                raise RuntimeError(
                    "Please provide a valid environment name [prd|stg|dev|uat|tst]!"
                )
        test_connection(connection)

    except RuntimeError as e:
        print(f"Error: {e}")
    finally:
        print("Exiting...")
