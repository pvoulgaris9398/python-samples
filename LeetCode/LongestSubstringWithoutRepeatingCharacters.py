# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def LengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window, anything between L and R
        # No duplicates in our window makes it "valid"
        # While window is valid move over "R"
        # While window is invalid move over "L"
        # Length = (left - right) + 1
        # Note at beginning, left = 0, right = 0
        # So, length = (0 - 0) + 1 = 1
        left = 0
        longest = 0
        chars = set()
        n = len(s)

        # O(n)
        for right in range(n):
            # Check for _invalidity_
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            # Now our window is valid again
            w = (right - left) + 1
            longest = max(longest, w)
            chars.add(s[right])

        return longest

    # Time: O(n)
    # Space: O(n)


def main():
    print("test")


if __name__ == "__main__":
    main()
