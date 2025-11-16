"""
WIP
"""


class Solution:
    def Solve(num: list[int], target: int) -> bool:
        return 66


def main():
    # Search for a value in a sorted array
    # Note, the array _MUST_ be sorted

    d = [1, 4, 6, 11, 22, 434, 543, 646, 722, 74, 850, 873, 899, 901, 999]

    target = 646

    r = Solution().Solve(d)

    # msg = "{target}%("was" if r else "was not")"

    print(f"target: {target}")
    print(f"result: {r}")


if __name__ == "__main__":
    main()
