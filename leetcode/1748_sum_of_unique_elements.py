from typing import List
from collections import defaultdict

# Runtime: 28 ms, faster than 94.08% of Python3 online submissions for Sum of Unique Elements.
# Memory Usage: 14.3 MB, less than 46.07% of Python3 online submissions for Sum of Unique Elements.
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        total_sum = 0
        counter = defaultdict(int)
        for num in nums:
            if num in counter and counter[num] == 1:
                total_sum -= num
                counter[num] += 1
            elif num not in counter:
                total_sum += num
                counter[num] += 1
        return total_sum
