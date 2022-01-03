class Solution:
    def isValid(self, s: str) -> bool:
        ending_chars = {"}": "{", ")": "(", "]": "["}
        stack = []
        for char in s:
            if char in ending_chars:
                if len(stack) == 0:
                    return False
                if stack[-1] != ending_chars[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0


if __name__ == "__main__":
    test_input = "()[]{}"
    result = Solution().isValid(test_input)
    print(result)
