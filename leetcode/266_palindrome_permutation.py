"""
If a odd length string can be re-organised into a Palindrome
it will have at most one character with odd count of appearances
within the string.

As such the problem is solved by simply determining whether their is only one
odd character count within the string
"""
from collections import defaultdict


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        mapping = defaultdict(int)
        for char in s:
            mapping[char] += 1
        count_odd = 0
        for value in mapping.values():
            count_odd += value % 2
        return count_odd <= 1


if __name__ == "__main__":
    result = Solution().canPermutePalindrome("ccos")
    assert result is False

    result = Solution().canPermutePalindrome("cco")
    assert result is True
