from utils import execute_and_log


class Solution:
    def compress(self, chars: list[str]) -> int:
        """
        https://leetcode.com/problems/string-compression/description/
        """

        if chars is None:
            raise ValueError("'chars' list variable but be non-null!")

        if len(chars) < 1:
            raise ValueError("'chars' list variable must contain at least one item!")

        # Keep track of current read/write location and input length
        read_index = 0
        write_index = 0
        array_length = len(chars)

        # Process input char by char
        while read_index < array_length:
            # Keep track of length of next group of characters
            # When the loop completes char_group_index points to the last character
            # of a group or to the end of the array/list
            # We only use it to index the array/list in the while condition
            # below which won't execute when it points past the end
            char_group_index = read_index + 1
            while (
                char_group_index < array_length
                and chars[char_group_index] == chars[read_index]
            ):
                # When we are at the last index, char_group_index will point past the end
                # of the list, but that's OK because that will give us the correct
                # count below
                char_group_index += 1

            # Write out the current char and increment the write pointer
            chars[write_index] = chars[read_index]
            write_index += 1

            # Check the count of characters
            count = char_group_index - read_index
            # Only output if greater than one (1) and handle
            # more than one digit
            if count > 1:
                digit_string = str(count)
                for digit in digit_string:
                    chars[write_index] = digit
                    write_index += 1

            # Reset read location to start of latest group
            read_index = char_group_index

        # Return latest write pointer, this will be length of the output
        # string
        return write_index


def test0():
    res, exc = execute_and_log(Solution().compress, None)
    print()


def test1():
    res, exc = execute_and_log(Solution().compress, [])
    print()


def test2():
    res, exc = execute_and_log(
        Solution().compress, ["a", "a", "a", "b", "b", "c", "c", "c"]
    )
    print()


def test3():
    res, exc = execute_and_log(
        Solution().compress, ["a", "a", "a", "b", "b", "c", "c", "d"]
    )
    print()


def test4():
    res, exc = execute_and_log(Solution().compress, ["a"])
    print()


def main():
    test0()
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    print()
    main()
