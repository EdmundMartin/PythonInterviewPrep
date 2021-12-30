from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        idx = 0
        output = []
        while idx < len(nums):
            freq = nums[idx]
            additional = [nums[idx + 1]] * freq
            output.extend(additional)
            idx += 2
        return output