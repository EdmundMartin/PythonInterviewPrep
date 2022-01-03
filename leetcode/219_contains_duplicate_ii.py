from typing import List
from collections import defaultdict


class Solution:
    def check_abs(self, indexes: List[int], k: int):
        if len(indexes) == 1:
            return False
        i = len(indexes) - 1
        while i > 0:
            if abs(indexes[i - 1] - indexes[i]) <= k:
                return True
            i -= 1
        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = defaultdict(list)
        for idx, num in enumerate(nums):
            mapping[num].append(idx)
        for value in mapping.values():
            if self.check_abs(value, k):
                return True
        return False


class SolutionFaster:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}
        for idx, num in enumerate(nums):
            if num in mapping:
                if abs(mapping[num] - idx) <= k:
                    return True
            mapping[num] = idx
        return False


if __name__ == "__main__":
    test_input = [1, 2, 3, 1]
    result = Solution().containsNearbyDuplicate(test_input, 3)
    assert result is True

    test_input = [1, 0, 1, 1]
    result = Solution().containsNearbyDuplicate(test_input, 1)
    assert result is True

    test_input = [1, 2, 3, 1, 2, 3]
    result = Solution().containsNearbyDuplicate(test_input, 2)
    assert result is False
