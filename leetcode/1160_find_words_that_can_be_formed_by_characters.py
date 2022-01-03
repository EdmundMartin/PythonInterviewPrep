from typing import List
from collections import defaultdict


class Solution:
    def can_create_word(self, word: str, counts) -> int:
        for ch in word:
            if ch not in counts:
                return 0
            if counts[ch] == 1:
                del counts[ch]
            else:
                counts[ch] -= 1
        return len(word)

    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = defaultdict(int)
        for char in chars:
            counts[char] += 1

        total_count = 0
        for word in words:
            tmp_count = counts.copy()
            total_count += self.can_create_word(word, tmp_count)
        return total_count


if __name__ == "__main__":
    result = Solution().countCharacters(["cat", "bt", "hat", "tree"])
