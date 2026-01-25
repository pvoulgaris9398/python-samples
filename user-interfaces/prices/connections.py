import os

from sqlalchemy import create_engine


def get_connection(env="dev"):
    match env:
        case "prd":
            return "prod-connection-string"
        case "dev":
            host = os.getenv("DBSERVER")
            dbname = os.getenv("DBNAME")
            user = os.getenv("DEVUSERNAME")
            password = os.getenv("DEVUSERPASSWORD")
            port = os.getenv("DBPORT")
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
