from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        results = set()
        for num in nums:
            if num not in results:
                results.add(num)
            else:
                results.remove(num)
        return list(results)[0]


if __name__ == '__main__':
    result = Solution().singleNumber([2, 2, 1])
    assert result == 1

    result = Solution().singleNumber([4, 1, 2, 1, 2])
    assert result == 4

    result = Solution().singleNumber([1])
    assert result == 1