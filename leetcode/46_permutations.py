from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []

        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first in permutation
                nums[first], nums[i] = nums[i], nums[first]

                backtrack(first + 1)

                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return output
