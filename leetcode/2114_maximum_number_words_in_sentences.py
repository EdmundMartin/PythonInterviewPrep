from typing import List


# Runtime: 36 ms, faster than 93.76% of Python3 online submissions for Maximum Number of Words Found in Sentences.
# Memory Usage: 14.2 MB, less than 89.60% of Python3 online submissions for Maximum Number of Words Found in Sentences.
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(s.split(' ')) for s in sentences])