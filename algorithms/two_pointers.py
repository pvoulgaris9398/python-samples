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


def test0():
    input = None
    result = is_palindrome(input)

    print(f"{input} {result}")


def test1():
    input = "abcdcba"
    result = is_palindrome(input)

    print(f"{input} {result}")


def test2():
    input = "amanaplanacanalpanama"
    result = is_palindrome(input)

    print(f"{input} {result}")


def test3():
    input = "kali"
    result = is_palindrome(input)

    print(f"{input} {result}")


def main():
    print("Two pointers example")
    test0()
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
