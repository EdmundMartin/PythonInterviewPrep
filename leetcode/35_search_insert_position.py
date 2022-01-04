from typing import List


def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        if target < nums[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return left


# Runtime: 40 ms, faster than 98.05% of Python3 online submissions for Search Insert Position.
# Memory Usage: 15.1 MB, less than 23.90% of Python3 online submissions for Search Insert Position.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return binary_search(nums, target)


if __name__ == "__main__":
    result = Solution().searchInsert([1, 3, 5, 6], 5)
    print(result)
