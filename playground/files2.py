import pandas as pd


def matches(row, field, value):
    if row[field] == value:
        return True
    return False


def compare(file1, file2):
    differences = []
    df1 = pd.read_csv("test1.csv", sep="|", index_col=False)
    df2 = pd.read_csv("test2.csv", sep="|", index_col=False)

    # For now, only include records in both files, by RECORD_ID
    v1 = [row for row in df2 if matches(row, "RECORD_ID", df1["RECORD_ID"])]

    print(v1)
    return differences
