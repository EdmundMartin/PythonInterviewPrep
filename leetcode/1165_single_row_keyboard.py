
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        last_idx = 0
        total_time = 0

        for ch in word:
            ch_index = keyboard.index(ch)
            dist = abs(last_idx - ch_index)
            total_time += dist
            last_idx = ch_index
        return total_time


if __name__ == '__main__':
    test_input = "abcdefghijklmnopqrstuvwxyz"
    result = Solution().calculateTime(test_input, "cba")
    assert result == 4

    test_input = "pqrstuvwxyzabcdefghijklmno"
    result = Solution().calculateTime(test_input, "leetcode")
    assert result == 73