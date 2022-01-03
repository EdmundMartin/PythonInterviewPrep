from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        permutation = []
        for idx in range(len(nums)):
            permutation.append(nums[nums[idx]])
        return permutation
