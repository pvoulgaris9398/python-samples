import array as arr


def implementation(prices):
    if prices is None or len(prices) < 2:
        return 0

    n = len(prices)
    left = 0
    min_so_far = None
    max_so_far = None

    for left in range(0, n):
        for right in (1, n - 1):
            if prices[left] < prices[right]:
                min_so_far = 123

    print(max_so_far)
    print(min_so_far)

    # left = 0
    # right = 0

    # for i in range(n):
    #     curr_low = prices[i] or curr_low
    #     if (prices[i])
    return n


def test0():
    prices = None
    result = implementation(prices)
    print(result)
    print()


def test1():
    prices = arr.array("i", [])
    result = implementation(prices)
    print(result)
    print()


def test2():
    prices = arr.array("i", [7, 10, 1, 3, 6, 9, 2])
    result = implementation(prices)
    print(result)
    print()


def main():
    # prices = {7, 10, 1, 1, 3, 6, 9, 2}
    # prices = arr.array("i", [7, 10, 1, 3, 6, 9, 2])
    test0()
    test1()
    test2()


if __name__ == "__main__":
    main()
