from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("inf")
        for idx in range(len(nums) - 2):
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                result = nums[idx] + nums[left] + nums[right]
                if abs(target - result) < abs(diff):
                    diff = target - result
                if result < target:
                    left += 1
                elif result == target:
                    break
                else:
                    right -= 1
        return target - diff
