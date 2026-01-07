import os
import sys
from pathlib import Path


def main():
    match sys.argv:
        case [_, file_path, search_string]:
            print(os.path.abspath(file_path))
            search_string(file_path, search_string)
        case _:
            print("Please pass a valid file path and name")


if __name__ == "__main__":
    main()


def search_string(file_path: str, search: str):
    try:
        with open(file_path, "r") as file:
            for line_num, line in enumerate(file, 1):
                if search in line:
                    yield (file_path, search, line_num)
    except FileNotFoundError:
        print(f"Error: File not found at: '{file_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")


def read_and_enumerate(file_path: str, search_string: str):
    file_name = Path(file_path).name
    with open(file_path, "r") as file:
        for line_num, line in enumerate(file):
            if search_string in line:
                yield (file_name, search_string, line_num)
