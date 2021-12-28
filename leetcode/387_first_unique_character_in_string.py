from collections import defaultdict


# Runtime: 116 ms, faster than 61.91% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 15.5 MB, less than 5.31% of Python3 online submissions for First Unique Character in a String.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_chars = defaultdict(list)
        for idx, char in enumerate(s):
            unique_chars[char].append(idx)
        first_idx = float('inf')
        for value in unique_chars.values():
            if len(value) == 1:
                first_idx = min(value[0], first_idx)
        return -1 if first_idx == float('inf') else first_idx
