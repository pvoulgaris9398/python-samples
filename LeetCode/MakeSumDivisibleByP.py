from utils import execute_and_log

"""
1590. Make Sum Divisible by P
https://leetcode.com/problems/make-sum-divisible-by-p/

"""


class Solution:
    def Solve(self, nums, p):
        k = sum(nums) % p
        if k == 0:
            return 0
        last = {0: -1}
        cur = 0
        ans = len(nums)
        for i, num in enumerate(nums):
            cur = (cur + num) % p
            target = (cur - k + p) % p

            if target in last:
                ans = min(ans, i - last[target])

            last[cur] = i

        if ans == len(nums):
            return -1
        else:
            return ans

    def SolveWithDebugging(self, nums, p, debug=False):
        k = sum(nums) % p
        if k == 0:
            return 0
        last = {0: -1}
        cur = 0
        ans = len(nums)
        for i, num in enumerate(nums):
            cur = (cur + num) % p
            target = (cur - k + p) % p

            if debug:
                print(f"p: {p}\tk: {k}\ti: {i}\tnum: {num}\tcur: {cur}")

            if target in last:
                if debug:
                    print(
                        f"ans: {ans}\ti: {i}\ttarget: {target}\tlast[target]: {last[target]}"
                    )
                print(last)
                ans = min(ans, i - last[target])

            last[cur] = i

        if ans == len(nums):
            return -1
        else:
            return ans


def test1():
    nums = [3, 1, 4, 2]
    p = 6
    expected = 1
    res, exc = execute_and_log(Solution().Solve, nums, p)
    print(f"Expected: {expected}\tActual: {res}")
    print()


def test2():
    nums = [6, 3, 5, 2]
    p = 9
    expected = 2
    res, exc = execute_and_log(Solution().Solve, nums, p)
    print(f"Expected: {expected}\tActual: {res}")
    print()


def test3():
    nums = [1, 2, 3]
    p = 3
    expected = 0
    res, exc = execute_and_log(Solution().Solve, nums, p)
    print(f"Expected: {expected}\tActual: {res}")
    print()


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    print()
    main()
