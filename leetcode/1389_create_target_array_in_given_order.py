from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        idx = 0
        while idx < len(nums):
            current_number = nums[idx]
            target_idx = index[idx]
            target.insert(target_idx, current_number)
            idx += 1
        return target


if __name__ == "__main__":

    res = Solution().createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1])
    print(res)
