from typing import List


# Runtime: 32 ms, faster than 72.32% of Python3 online submissions for Reverse Words in a String.
# Memory Usage: 14.5 MB, less than 39.50% of Python3 online submissions for Reverse Words in a String.
class Solution:

    def split_words(self, s: str) -> List[str]:
        words = []
        current_word = ""
        for char in s:
            if char != " ":
                current_word += char
            else:
                if len(current_word) > 0:
                    words.append(current_word)
                current_word = ""
        if len(current_word) > 0:
            words.append(current_word)
        return words

    def reverse_list(self, words: List[str]) -> str:
        i = 0
        j = len(words) - 1
        while i < j:
            words[i], words[j] = words[j], words[i]
            i += 1
            j -= 1
        return ' '.join(words)

    def reverseWords(self, s: str) -> str:
        words = self.split_words(s)
        return self.reverse_list(words)


if __name__ == '__main__':
    s = Solution().reverseWords("the sky is blue")
    assert s == "blue is sky the"