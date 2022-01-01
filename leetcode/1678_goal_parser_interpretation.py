

# Runtime: 28 ms, faster than 80.54% of Python3 online submissions for Goal Parser Interpretation.
# Memory Usage: 14.1 MB, less than 88.85% of Python3 online submissions for Goal Parser Interpretation.
class Solution:
    def interpret(self, command: str) -> str:
        idx = 0
        output = ""
        while idx < len(command):
            char = command[idx]
            if char == 'G':
                output += char
                idx += 1
            elif char == '(' and command[idx + 1] == ')':
                output += "o"
                idx += 2
            elif char == '(' and command[idx + 1] == "a":
                output += "al"
                idx += 4
        return output


if __name__ == '__main__':
    result = Solution().interpret("G()()()()(al)")
    assert result == "Gooooal"

    result = Solution().interpret("G()(al)")
    assert result == "Goal"

    result = Solution().interpret("(al)G(al)()()G")
    assert result == "alGalooG"