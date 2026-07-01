from itertools import combinations, combinations_with_replacement

if __name__ == "__main__":
    print("Enter 'n':")
    n = input()

    print(n)

    print("Enter 'k':")

    k = input()
    print(k)

    data = ["a", "a", "b", "c"]

    indices = range(1, len(data) + 1)  # 1-based index

    index_pairs = list(combinations(indices, 2))

    index_pairs2 = list(combinations_with_replacement(data, 2))

    print(index_pairs2)

"""
    result: list[tuple(int, int)] = []

    data = ["a", "a", "b", "c"]

    for i in range(0, len(data) - 1):
        for j in range(i, len(data)):
            result.append((range[i], range[j]))
"""
