from typing import List


# Runtime: 48 ms, faster than 67.47% of Python3 online submissions for Find Target Indices After Sorting Array.
# Memory Usage: 14.3 MB, less than 55.10% of Python3 online submissions for Find Target Indices After Sorting Array.
class Solution:

    def find_first(self, nums: List[int], target):
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

    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        first_idx = self.find_first(nums, target)
        if first_idx == -1:
            return []
        indexes = [first_idx]
        next_idx = first_idx + 1
        while next_idx < len(nums) and nums[next_idx] == target:
            indexes.append(next_idx)
            next_idx += 1
        return indexes
