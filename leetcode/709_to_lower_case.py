

from string import ascii_uppercase


class Solution:
    def toLowerCase(self, s: str) -> str:
        mapping = {}
        for k in ascii_uppercase:
            mapping[k] = k.lower()
        result = ""
        for char in s:
            if char in mapping:
                result += mapping[char]
            else:
                result += char
        return result
