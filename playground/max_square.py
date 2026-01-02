from collections import deque  # noqa: F401


def largest_square(bin_array: list[list[int]]) -> int:
    n = len(bin_array)
    m = len(bin_array[0])
    dp = [[n] * 0 for i in range(m)]

    print(f"[n] = {n}\t[m] = {m}")

    for i in range(n):
        for j in range(m):
            print(f"[i] = {i}\t[j] = {j}")
            if bin_array[i][j] == 0:
                continue
            left = right = diag = 0
            if i > 0:
                left = dp[i - 1][j]
            if j > 0:
                right = dp[i][j - 1]
            if i > 0 and j > 0:
                diag = dp[i - 1][j - 1]
            dp[i][j] = min([left, right, diag]) + 1
    rowwise_max = [max(row) for row in dp]
    return max(rowwise_max)


def is_inside(cell: tuple[int, int], matrix: list[list[int]]) -> bool:
    row, col = cell
    return row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0])


def value_at(cell: tuple[int, int], matrix: list[list[int]]) -> int:
    row, col = cell
    return matrix[row][col]


def is_valid_neighbor(cell: tuple[int, int], matrix: list[list[int]]) -> bool:
    return is_inside(cell, matrix) and value_at(cell, matrix) == 1


def has_valid_neighbors(cell: tuple[int, int], matrix: list[list[int]]) -> bool:
    row, col = cell
    return (
        is_valid_neighbor(row + 1, col)
        and is_valid_neighbor(0, col + 1)
        and is_valid_neighbor(row + 1, col + 1)
    )


def largest_square2(bin_array: list[list[int]]) -> int:
    n = len(bin_array)
    m = len(bin_array[0])

    candidates = {}  # noqa: F841

    for i in range(n):
        for j in range(m):
            if value_at((i, j)) == 0:
                continue

    pass


def test0():
    bin_array = [
        [0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
    ]
    max = largest_square(bin_array)
    print(f"Max: {max}")


def main():
    test0()


if __name__ == "__main__":
    main()
