from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        sums = [nums[0]]
        for i in range(1, len(nums)):
            new_sum = sums[i - 1] + nums[i]
            sums.append(new_sum)
        return sums


if __name__ == '__main__':
    result = Solution().runningSum([1, 2, 3, 4])
    print(result)

    result = Solution().runningSum([1, 1, 1, 1, 1])
    print(result)

    result = Solution().runningSum([3, 1, 2, 10, 1])
    print(result)