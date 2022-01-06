from typing import List


class Solution:

    def is_palindrome(self, target: str) -> bool:
        reversal_target = list(target)
        i = 0
        j = len(reversal_target) - 1
        while i < j:
            reversal_target[i], reversal_target[j] = reversal_target[j], reversal_target[i]
            i += 1
            j -= 1
        return "".join(reversal_target) == target

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.is_palindrome(word):
                return word
        return ""
