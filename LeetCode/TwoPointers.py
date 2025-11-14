# https://leetcode.com/problems/3sum/description/
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        h = {}  # num : index
        n = len(nums)
        s = set()

        # Build hashmap of keys (num) and their associated values (i: index)
        for i, num in enumerate(nums):
            h[num] = i

        for i in range(n):
            for j in range(i + 1, n):
                # Number we are looking for
                desired = -nums[i] - nums[j]
                # Make sure we don't have i=j, i=k, j=k:
                if desired in h and h[desired] != i and h[desired] != j:
                    s.add(tuple(sorted(nums[i], nums[j], desired)))

        return s

        # Time: O(n^2)
        # Space: O(n)
