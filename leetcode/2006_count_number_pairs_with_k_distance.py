from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(nums):
            for j in range(1, nums):
                if i < j and abs(nums[i] - nums[j]) == k:
                    count += 1
        return count


class SolutionAlternative:
    def countKDifference(self, nums: List[int], k: int) -> int:
        mapping = {}
        for idx, num in enumerate(nums):
            if num not in mapping:
                mapping[num] = [idx]
            else:
                mapping[num].append(idx)

        count = 0
        for idx, num in enumerate(nums):
            bigger = num + k
            smaller = num - k
            if bigger in mapping:
                count += sum([1 for v in mapping[bigger] if v > idx])
            if smaller in mapping:
                count += sum([1 for v in mapping[smaller] if v > idx])

        return count
