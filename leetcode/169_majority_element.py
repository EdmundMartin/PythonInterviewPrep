from typing import List


# Runtime: 166 ms, faster than 62.44% of Python3 online submissions for Majority Element.
# Memory Usage: 15.4 MB, less than 82.39% of Python3 online submissions for Majority Element.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        majority = len(nums) / 2
        current_count = 1
        prev = nums[0]
        for num in nums[1:]:
            if num == prev:
                current_count += 1
                if current_count >= majority:
                    return num
            else:
                prev = num
                current_count = 1


if __name__ == '__main__':
    result = Solution().majorityElement([3, 2, 3])
    assert result == 3

    result = Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])
    assert result == 2