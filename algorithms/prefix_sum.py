def sum_of_numbers_in_range(array: list[int], i, j):
    if array is None or len(array) == 0 or i < 0 or j < 0 or j < i:
        return -1
    result = build_prefix_sum_array(array)

    return result[j] + result[i - 1]


def build_prefix_sum_array(array: list[int]):
    n = len(array)
    result = [0] * n
    sum_so_far = 0
    for i in range(0, n):
        sum_so_far = sum_so_far + array[i]
        result[i] = sum_so_far
    return result


"""
Test bounds/handing of the function
"""


def test0():
    print(sum_of_numbers_in_range(None, 0, 0))
    print(sum_of_numbers_in_range([], 0, 0))
    print(sum_of_numbers_in_range([], -1, -1))
    print(sum_of_numbers_in_range([1, 2, 3], 2, 1))


"""
Actual functional test
"""


def test1():
    input = [1, 2, 3, 4, 5, 6, 7]
    i = 2
    j = 4
    result = sum_of_numbers_in_range(input, i, j)

    print(result)


"""
Query for sum of elements in a sub-array
"""


def main():
    print("Prefix sum example")
    test0()
    test1()


if __name__ == "__main__":
    main()
