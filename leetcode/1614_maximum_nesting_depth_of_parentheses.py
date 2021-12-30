

class Solution:
    def maxDepth(self, s: str) -> int:
        starting_paren = "("
        ending_paren = ")"
        stack = []
        max_depth = 0
        for ch in s:
            if ch == starting_paren:
                stack.append(starting_paren)
            elif ch == ending_paren:
                stack.pop()
            max_depth = max(max_depth, len(stack))
        return max_depth


if __name__ == '__main__':
    test_input = "(1+(2*3)+((8)/4))+1"
    result = Solution().maxDepth(test_input)
    print(result)

    test_input = "(1)+((2))+(((3)))"
    result = Solution().maxDepth(test_input)
    print(result)