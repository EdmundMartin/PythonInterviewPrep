from typing import List


# Runtime: 232 ms, faster than 81.27% of Python3 online submissions for Binary Search.
# Memory Usage: 15.7 MB, less than 28.71% of Python3 online submissions for Binary Search.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1


if __name__ == '__main__':
    test_one = [-1, 0, 3, 5, 9, 12]

    result = Solution().search(test_one, 9)
    assert result == 4

    test_two = [-1, 0, 3, 5, 9, 12]
    result = Solution().search(test_two, 2)
    assert result == -1
