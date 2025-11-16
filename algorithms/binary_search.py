"""
WIP
"""


class Solution:
    def Solve(nums: list[int], target: int) -> bool:
        start = 0
        end = len(nums)
        i = (start - end) / 2
        while start <= end:
            if target == nums[i]:
                return True
            if target > nums[i]:
                start = i
            else:
                end = i - 1

            i = (start - end) / 2

        return False


def binary_search(arr: list[int], target: int, feasible) -> int:
    left, right = (0, len(arr) - 1)
    first_true_index = -1
    while left <= right:
        mid = (left + right) / 2
        if feasible(mid):
            first_true_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return first_true_index


def main():
    # Search for a value in a sorted array
    # Note, the array _MUST_ be sorted

    d = [1, 4, 6, 11, 22, 434, 543, 646, 722, 74, 850, 873, 899, 901, 999]

    target = 646

    result = binary_search(d, target, lambda x: x >= target)

    print(f"target: {target}")
    print(f"result: {result}")


"""
    r = Solution().Solve(d)

    # msg = "{target}%("was" if r else "was not")"

    print(f"target: {target}")
    print(f"result: {r}")
"""

if __name__ == "__main__":
    main()
