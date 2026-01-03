def find_larest(input):
    max_so_far = 0
    for i in range(len(input)):
        max_so_far = max(max_so_far, input[i])

    return max_so_far


def test0():
    input = [2, 5, 20, 30, 56]
    result = find_larest(input)
    print(f"Max: '{result}'")
    pass


def main():
    test0()


if __name__ == "__main__":
    main()
