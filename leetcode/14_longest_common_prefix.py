from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min([len(s) for s in strs])
        idx = 0
        longest_prefix = ""
        while idx < shortest_word:
            current_char = strs[0][idx]
            if all([s[idx] == current_char for s in strs]):
                longest_prefix += current_char
            else:
                break
            idx += 1
        return longest_prefix


if __name__ == "__main__":
    test_input = ["flower", "flow", "flight"]
    result = Solution().longestCommonPrefix(test_input)
    assert result == "fl"

    test_input = ["dog", "racecar", "car"]
    result = Solution().longestCommonPrefix(test_input)
    assert result == ""
