from typing import List
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        chars = defaultdict(0)

        left = 0
        right = 0

        result = 0

        while right < len(s):
            current_char = s[right]
            chars[current_char] += 1

            while chars[current_char] > 1:
                left_char = s[left]
                chars[left_char] -= 1
                left += 1

            result = max(result, right - left + 1)

            right += 1
        return result


class SolutionAlternative:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0
        while right < len(s):
            chars = {}
            for i in range(left, right + 1):
                if s[i] in chars:
                    chars[s[i]] += 1
                else:
                    chars[s[i]] = 1

            if max(chars.values()) > 1:
                left += 1
            else:
                right += 1
                max_length = max(max_length, len(chars))
        return max_length


class SolutionStack:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        result = 0
        for idx, char in enumerate(s):
            if char not in stack:
                stack.append(char)
                result = max(result, len(stack))
            else:
                stack.append(char)
                stack = stack[stack.index(char) + 1 :]
        return result


class SolutionMine:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0
        while right < len(s):
            chars = set()
            found_duplicate = False

            for i in range(left, right + 1):
                current_char = s[i]
                if current_char in chars:
                    found_duplicate = True
                    break
                else:
                    chars.add(current_char)

            if found_duplicate:
                left += 1
            else:
                right += 1
                max_length = max(max_length, len(chars))
        return max_length
