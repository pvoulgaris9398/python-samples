def is_palindrome(s: str) -> bool:
    if s is None:
        return False
    left = 0
    right = len(s) - 1
    while left < right:
        # TODO: Handle whitespace, punctuation, etc.
        if s[left] != s[right]:
            return False

        left = left + 1
        right = right - 1

    return True


"""
Using generalized version of "two-pointer" algorithm
"""


def is_palindrome_2(s: str) -> bool:
    if s is None:
        return False

    def next_left_index(s: str, left):
        return left + 1

    def next_right_index(s: str, right):
        return right - 1

    def check_condition(left_value, right_value):
        return left_value == right_value

    return two_pointer_template2(s, next_left_index, next_right_index, check_condition)


"""
Generalized version(s) the algorithm
"""


def two_pointer_template2(
    input: list, next_left_index, next_right_index, check_condition
):
    left = 0
    right = len(input) - 1
    while left < right:
        left = next_left_index(input, left)
        right = next_right_index(input, right)
        if not check_condition(input[left], input[right]):
            return False

    return True


def two_pointer_template1(input: list, is_valid, check_condition):
    left = 0
    right = len(input) - 1
    while left < right:
        while not is_valid(input[left]):
            left = left + 1
        while not is_valid(input[right]):
            right = right - 1
        if not check_condition(input[left], input[right]):
            return False
        left = left + 1
        right = right - 1

    return True


def test0():
    input = None
    result = is_palindrome(input)

    print(f"(is_palindrome): {input} {result}")


def test1():
    input = "abcdcba"
    result = is_palindrome(input)

    print(f"(is_palindrome): {input} {result}")


def test2():
    input = "amanaplanacanalpanama"
    result = is_palindrome(input)

    print(f"(is_palindrome): {input} {result}")


def test3():
    input = "kali"
    result = is_palindrome(input)

    print(f"(is_palindrome): {input} {result}")


def test4():
    input = "kali"
    result = is_palindrome_2(input)

    print(f"(is_palindrome_2): {input} {result}")


def test5():
    input = "abcdcba"
    result = is_palindrome_2(input)

    print(f"(is_palindrome_2): {input} {result}")


def main():
    print("Two pointers example")
    test0()
    test1()
    test2()
    test3()
    test4()
    test5()


if __name__ == "__main__":
    main()
