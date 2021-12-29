

class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, "X": 10, "V":5, "I":1}
        total = 0
        for i in range(len(s)):
            int_val = nums[s[i]]
            if i + 1 < len(s) and nums[s[i+1]] > int_val:
                total -= int_val
            else:
                total += int_val
        return total
