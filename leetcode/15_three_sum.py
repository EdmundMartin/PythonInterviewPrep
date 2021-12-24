from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        target = 0
        seen = set()
        for idx in range(len(nums) - 2):
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[idx] + nums[left] + nums[right]
                if current_sum == target:
                    if (nums[idx], nums[left], nums[right]) not in seen:
                        results.append([nums[idx], nums[left], nums[right]])
                        seen.add((nums[idx], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
        return results


if __name__ == '__main__':
    test_array = [-1, 0, 1, 2, -1, -4]
    result = Solution().threeSum(test_array)
    assert result == [[-1, -1, 2], [-1, 0, 1]]