import csv  # noqa: F401
import os

import pandas as pd


def analyze(file1, file2, key: list[str], names: list[str], sep="|"):
    filename1 = os.path.basename(file1)  # noqa: F841
    filename2 = os.path.basename(file2)  # noqa: F841

    df1 = pd.read_csv(
        file1, dtype={"FIELD-NAME-1": object, "FIELD-NAME-2": object}, sep=sep
    )

    df2 = pd.read_csv(
        file2, dtype={"FIELD-NAME-1": object, "FIELD-NAME-2": object}, sep=sep
    )

    df1 = pd.DataFrame(df1, columns=key)
    df2 = pd.DataFrame(df2, columns=key)

    print_spacer()


def print_spacer(character="*", n=80):
    repeated_char = character * n
    print()
    print(repeated_char)


def determine_diffs_v1(
    left: pd.DataFrame,
    right: pd.DataFrame,
    key: list[str] = ["key-field-1", "key-field-2"],
):
    left = pd.DataFrame(left, columns=key)
    right = pd.DataFrame(right, columns=key)

    return pd.concat([left, right]).drop_duplicates(keep=False)


def determine_diffs_v2(
    left: pd.DataFrame,
    right: pd.DataFrame,
    left_name: str,
    right_name: str,
    key: list[str] = ["key-field-1", "key-field-2"],
    identifiers: list[str] = ["left-only", "right-only"],
):
    merged_df1 = left.merge(right, on=key, how="left", indicator=True)

    left_only = merged_df1[merged_df1["_merge"] == "left_only"].drop(columns="_merge")
    left_only.insert(0, "Source", left_name)
    left_only.insert(1, "Idenifier", identifiers[0])

    print(left_only)

    merged_df2 = right.merge(left, on=key, how="left", indicator=True)

    right_only = merged_df2[merged_df2["_merge"] == "left_only"].drop(columns="_merge")
    right_only.insert(0, "Source", left_name)
    right_only.insert(1, "Idenifier", identifiers[1])

    final = pd.merge(left_only, right_only, how="outer")

    return final
