from utils import execute_and_log

"""
1590. Make Sum Divisible by P
https://leetcode.com/problems/make-sum-divisible-by-p/

"""


class Solution:
    def Solve():
        print("Solve")


def test1():
    nums = [3, 1, 4, 2]
    p = 6
    expected = 1
    print("Test1")
    res, exc = execute_and_log(Solution().Solve, nums, p)
    print(f"Expected: {expected}\tActual: {res}")


def main():
    test1()


if __name__ == "__main__":
    print()
    main()
