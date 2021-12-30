from typing import List


class Solution:

    def flatten(self, words: List[str]):
        result = ""
        for word in words:
            result += word
        return result

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word_one_length = sum([len(w) for w in word1])
        if word_one_length != sum([len(w) for w in word2]):
            return False
        one_combined = self.flatten(word1)
        two_combined = self.flatten(word2)
        idx = 0
        while idx < word_one_length:
            if one_combined[idx] != two_combined[idx]:
                return False
            idx += 1
        return True
