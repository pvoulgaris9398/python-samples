from collections import Counter

from utils import execute_and_log

"""
974. Subarray Sums Divisible by K
https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
"""


class Solution:
    def Solve(self, nums: list[int], k: int, debug: bool = False) -> int:
        remainder_count = Counter({0: 1})

        result = 0
        prefix_sum = 0

        for num in nums:
            if debug:
                print(remainder_count)

            # Note no special-handling for negative numbers needed with Python
            # and the modulo operator here
            prefix_sum = (prefix_sum + num) % k

            result += remainder_count[prefix_sum]

            remainder_count[prefix_sum] += 1

            if debug:
                print(remainder_count)

        return result


def test0():
    res, exc = execute_and_log(Solution().Solve, [5], 9)
    print()


def test1():
    res, exc = execute_and_log(Solution().Solve, [3, 1, 2, 5, 1], 3)
    print()


def test2():
    res, exc = execute_and_log(Solution().Solve, [4, 5, 0, -2, -3, 1], 5)
    print()


def main():
    test0()
    test1()
    test2()


if __name__ == "__main__":
    print()
    main()
