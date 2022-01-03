from typing import List
from random import shuffle


class Solution:
    def quick_sort(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums
        pivot = nums[0]
        smaller = []
        partition = [pivot]
        larger = []
        for i in range(1, len(nums)):
            if nums[i] == pivot:
                partition.append(nums[i])
            elif nums[i] > pivot:
                larger.append(nums[i])
            else:
                smaller.append(nums[i])
        return self.quick_sort(smaller) + partition + self.quick_sort(larger)

    def sortArray(self, nums: List[int]) -> List[int]:
        shuffle(nums)  # Avoids quicksorts worse time complexity
        return self.quick_sort(nums)
