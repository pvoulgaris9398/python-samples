"""
Find the smallest element in the array
and exchange it with the element in the first position
Find the second smallest element in the array
and exchange it with the element in the second position
"""

"""
Returns the smallest value in the provided array
"""


def find_min_value(arr):
    min_index = 0
    for i in range(len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    return arr[min_index]


def find_min_index(arr, start_index):
    min_index = start_index
    for i in range(start_index + 1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    return min_index


def sort(arr):
    for i in range(len(arr) - 1):
        min_index = find_min_index(arr, i)
        (arr[i], arr[min_index]) = (arr[min_index], arr[i])


def test0():
    arr = [5, 3, 55, 25, 4, 67, 2, 88, 6]
    min_value = find_min_value(arr)
    print(f"Smallest (minimum) value: {min_value}")


def test1():
    arr = [5, 3, 55, 25, 4, 67, 2, 88, 6]
    print(arr)
    sort(arr)
    print(f"Sorted: {all([arr[i] <= arr[i + 1] for i in range(len(arr) - 1)])}")
    print(arr)


def test2():
    arr = [-4, 2, 5, 8, -7, 3, 6, -1, 7]
    print(arr)
    sort(arr)
    print(f"Sorted: {all([arr[i] <= arr[i + 1] for i in range(len(arr) - 1)])}")
    print(arr)


def main():
    test0()
    test1()
    test2()


if __name__ == "__main__":
    main()
