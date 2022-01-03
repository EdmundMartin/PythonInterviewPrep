from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        prev = nums[0]
        for num in nums[1:]:
            if num == prev:
                return
            prev = num
        return True


if __name__ == "__main__":
    problem_input = [1, 2, 3, 1]
    result = Solution().containsDuplicate(problem_input)
    print(result)
