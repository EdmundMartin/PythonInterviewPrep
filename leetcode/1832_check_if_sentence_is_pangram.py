from string import ascii_lowercase


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        all_chars = set(ascii_lowercase)
        for char in sentence:
            if char in all_chars:
                all_chars.remove(char)
        return len(all_chars) == 0


if __name__ == '__main__':
    Solution().checkIfPangram("hello")