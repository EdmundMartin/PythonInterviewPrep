from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        left_idx = self.find_lower(nums, target)
        if left_idx == -1:
            return [-1, -1]
        right_idx = self.find_upper(nums, target)
        return [left_idx, right_idx]

    def find_lower(self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                if middle == left or nums[middle - 1] < target:
                    return middle
                right = middle - 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1

    def find_upper(self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                if middle == right or nums[middle + 1] > target:
                    return middle
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1
