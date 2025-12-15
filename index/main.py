from pathlib import Path


def main():
    # TODO: Extract command-line arguments, if any
    file_path = r"C:\Users\Peter\_temp"
    for dir in enumerate_directories(file_path):
        print(f"{dir}")


def enumerate_directories(file_path):
    [arg1 for arg1, _, _ in Path.walk(Path(file_path))]
    # for arg1, arg2, arg3 in Path.walk(Path(file_path)):
    #     print(f"{arg1}")


if __name__ == "__main__":
    main()
