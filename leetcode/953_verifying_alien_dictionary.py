from typing import List, Dict


# Runtime: 60 ms, faster than 6.15% of Python3 online submissions for Verifying an Alien Dictionary.
# Memory Usage: 14.2 MB, less than 91.24% of Python3 online submissions for Verifying an Alien Dictionary.
class Solution:

    def compare_words(self, first: str, second: str, order_mapping: Dict[str, int]):
        idx = 0
        while idx < len(first) and idx < len(second):
            if order_mapping[first[idx]] > order_mapping[second[idx]]:
                return False
            if order_mapping[first[idx]] < order_mapping[second[idx]]:
                return True
            idx += 1
        if len(second) == len(first):
            return True
        return len(second) > len(first)

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_mapping = {}
        for idx, val in enumerate(order):
            order_mapping[val] = idx

        for idx in range(len(words) - 1):
            if not self.compare_words(words[idx], words[idx + 1], order_mapping):
                return False
        return True


if __name__ == '__main__':
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    result = Solution().isAlienSorted(words, order)
    assert result is True

    words = ["word", "world", "row"]
    order = "worldabcefghijkmnpqstuvxyz"
    result = Solution().isAlienSorted(words, order)
    assert result is False

    words = ["apple", "app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    result = Solution().isAlienSorted(words, order)
    assert result is False
