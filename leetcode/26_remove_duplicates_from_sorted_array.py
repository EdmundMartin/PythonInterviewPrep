from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1


if __name__ == "__main__":
    test_array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result = Solution().removeDuplicates(test_array)
    assert result == 5
    assert test_array == [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
