from typing import List


# Runtime: 36 ms, faster than 94.11% of Python3 online submissions for Two Sum Less Than K.
# Memory Usage: 14.3 MB, less than 55.22% of Python3 online submissions for Two Sum Less Than K.
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        current_max = float('-inf')
        while i < j:
            current_sum = nums[i] + nums[j]
            if current_sum < k:
                current_max = max(current_sum, current_max)
                i += 1
            else:
                j -= 1
        return -1 if current_max == float('-inf') else current_max


if __name__ == '__main__':
    nums = [34, 23, 1, 24, 75, 33, 54, 8]
    k = 60
    result = Solution().twoSumLessThanK(nums, k)
    assert result == 58

    nums = [10, 20, 30]
    k = 15
    result = Solution().twoSumLessThanK(nums, 15)
    assert result == -1