class Solution:
    def removeDuplicates(self, s: str) -> str:
        output = []
        for char in s:
            if len(output) > 0 and char == output[-1]:
                output.pop()
            else:
                output.append(char)
        return "".join(output)


if __name__ == "__main__":
    result = Solution().removeDuplicates("abbaca")
    assert result == "ca"

    result = Solution().removeDuplicates("azxxzy")
    assert result == "ay"
