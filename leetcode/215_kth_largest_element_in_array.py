from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left: int, right: int, pivot_idx: int):
            pivot = nums[pivot_idx]

            # Move pivot to final index
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            # Move all smaller elements to left
            store_idx = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1

            nums[right], nums[store_idx] = nums[store_idx], nums[right]

            return store_idx

        def select(left, right, k_smallest):
            if left == right:
                return nums[left]

            pivot_idx = random.randint(left, right)

            pivot_idx = partition(left, right, pivot_idx)

            if k_smallest == pivot_idx:
                return nums[k_smallest]
            elif k_smallest < pivot_idx:
                return select(left, pivot_idx - 1, k_smallest)
            else:
                return select(pivot_idx + 1, right, k_smallest)

        return select(0, len(nums) - 1, len(nums) - k)
