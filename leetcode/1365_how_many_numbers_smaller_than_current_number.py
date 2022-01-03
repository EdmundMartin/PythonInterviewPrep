from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = nums[::]
        sorted_nums.sort()
        result = []
        for num in nums:
            idx = sorted_nums.index(num)
            result.append(idx)
        return result


if __name__ == "__main__":
    nums = [8, 1, 2, 2, 3]
    result = Solution().smallerNumbersThanCurrent(nums)
    assert result == [4, 0, 1, 1, 3]
