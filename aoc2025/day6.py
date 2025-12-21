# import numpy as np
import pandas as pd


def read_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line


def process(filename):
    for line in read_file(filename):
        print(line)


def main():
    filename = r"./aoc2025/data/day6-test.txt"

    # data = pd.DataFrame(np.loadtxt(filename, dtype=str))
    data = pd.read_table(filename, header=None, index_col=False)
    print(data)
    print()

    all_but_last = data.iloc[:-1]
    print(all_but_last)
    print()

    last = data.tail(1)
    print(last)
    print()


if __name__ == "__main__":
    main()
